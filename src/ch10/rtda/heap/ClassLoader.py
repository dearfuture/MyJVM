#!/usr/bin/env python
# encoding: utf-8
from pydoc import resolve
from types import new_class

from classfile.ClassFile import ClassFile
from classpath.ClassPath import ClassPath
from rtda.Slot import Slots
from rtda.heap import AccessFlags
from rtda.heap.Class import Class
from rtda.heap.ClassNameHelper import ClassNameHelper
from rtda.heap.Field import Field
from rtda.heap import StringPool


class ClassLoader:

    def __init__(self, class_path: ClassPath, verbose_flag: bool):
        self.class_path = class_path
        self.class_map = dict()
        self.verbose_flag = verbose_flag

    @staticmethod
    def new_class_loader(class_path: ClassPath, verbose_flag: bool):
        class_loader = ClassLoader(class_path, verbose_flag)
        class_loader.load_basic_classes()
        class_loader.load_primitive_classes()
        return class_loader

    def load_basic_classes(self):
        jl_class_class = self.load_class("java/lang/Class")
        for clazz in self.class_map.values():
            if clazz.j_class is None:
                clazz.j_class = jl_class_class.new_object()
                clazz.j_class.extra = clazz

    def load_class(self, class_name):
        clazz = self.class_map.get(class_name)
        if clazz:
            # 如果已经缓存
            return clazz

        # 数组类
        if class_name[0] == '[':
            clazz = self.load_array_class(class_name)
        else:
            clazz = self.load_non_array_class(class_name)

        jl_class_class = self.class_map.get("java/lang/Class")
        if jl_class_class:
            clazz.j_class = jl_class_class.new_object()
            clazz.j_class.extra = clazz
        return clazz

    def load_non_array_class(self, class_name, verbose=False):
        data, entry = self.read_class(class_name)
        clazz = self.define(data)
        ClassLoader.link(clazz)
        if self.verbose_flag:
            print("[Loaded {0} from {1}]".format(class_name, entry))
        return clazz

    def load_primitive_classes(self):
        for primitive_type in ClassNameHelper.primitive_types.keys():
            self.load_primitive_class(primitive_type)

    def load_primitive_class(self, class_name):
        clazz = Class()
        clazz.access_flags= AccessFlags.ACC_PUBLIC
        clazz.name = class_name
        clazz.loader = self
        clazz.init_started = True

        clazz.j_class = self.class_map.get("java/lang/Class").new_object()
        clazz.j_class.extra = clazz
        self.class_map[class_name] = clazz

    def read_class(self, class_name):
        data, entry, error = self.class_path.read_class(class_name)
        if error:
            raise RuntimeError("java.lang.ClassNotFoundException: " + class_name)
        # entry: 为了打印类加载信息，把最终加载class文件的类路径项也返回给调用者
        return data, entry

    def define(self, data: bytes):
        clazz = ClassLoader.parse_class(data)

        # 设置loader
        clazz.loader = self

        ClassLoader.resolve_super_class(clazz)
        ClassLoader.resolve_interfaces(clazz)

        # 缓存结果
        self.class_map[clazz.name] = clazz
        return clazz


    @staticmethod
    def parse_class(data: bytes):
        class_file = ClassFile.parse(data)
        return Class.new_class(class_file)

    @staticmethod
    def resolve_super_class(clazz: Class):
        if clazz.name != "java/lang/Object":
            clazz.super_class = clazz.loader.load_class(clazz.super_class_name)

    @staticmethod
    def resolve_interfaces(clazz: Class):
        interface_count = len(clazz.interface_names)
        if interface_count > 0:
            for interfaceName in clazz.interface_names:
                clazz.interfaces.append(clazz.loader.load_class(interfaceName))


    @staticmethod
    def link(clazz: Class):
        # ClassLoader.verify(clazz)
        ClassLoader.prepare(clazz)

    @staticmethod
    def prepare(clazz: Class):
        ClassLoader.calc_instance_field_slot_ids(clazz)
        ClassLoader.calc_static_field_slot_ids(clazz)
        ClassLoader.alloc_and_init_static_vars(clazz)


    @staticmethod
    def calc_instance_field_slot_ids(clazz: Class):
        slot_id = 0
        if clazz.super_class:
            slot_id = clazz.super_class.instance_slot_count
        for field in clazz.fields:
            if not field.is_static():
                # 编号
                field.slot_id = slot_id
                slot_id += 1
                if field.is_long_or_double():
                    slot_id += 1
        clazz.instance_slot_count = slot_id

    @staticmethod
    def calc_static_field_slot_ids(clazz: Class):
        slot_id = 0
        if clazz.super_class:
            slot_id = clazz.super_class.instance_slot_count
        for field in clazz.fields:
            if  field.is_static():
                # 编号
                field.slot_id = slot_id
                slot_id += 1
                if field.is_long_or_double():
                    slot_id += 1
        clazz.static_slot_count = slot_id

    @staticmethod
    def alloc_and_init_static_vars(clazz: Class):
        clazz.static_vars = Slots(clazz.static_slot_count)
        for field in clazz.fields:
            if field.is_static() and field.is_final():
                ClassLoader.init_static_final_var(clazz, field)

    @staticmethod
    def init_static_final_var(clazz: Class, field: Field):
        static_vars = clazz.static_vars
        rt_constant_pool = clazz.rt_constant_pool
        index = field.const_value_index
        slot_id = field.slot_id

        if index > 0:
            type = field.descriptor
            if type in {"Z", "B", "C", "S", "I", "J"}:
                val = rt_constant_pool.get_constant(index)
                static_vars.set_numeric(slot_id, val)

            elif type == "D":
                val = rt_constant_pool.get_constant(index)
                static_vars.set_double(slot_id, val)
            elif type == "F":
                val = rt_constant_pool.get_constant(index)
                static_vars.set_float(slot_id, val)

            elif type == "Ljava/lang/String;":
                py_str = rt_constant_pool.get_constant(index)
                jstr = StringPool.j_string(clazz.loader, py_str)
                static_vars.set_ref(slot_id, jstr)

    # 数组类
    def load_array_class(self, class_name):
        clazz = Class()

        clazz.access_flags = AccessFlags.ACC_PUBLIC
        clazz.name = class_name
        clazz.loader = self
        clazz.init_started = True
        clazz.super_class = self.load_class("java/lang/Object")
        clazz.interfaces = [self.load_class("java/lang/Cloneable"), self.load_class("java/io/Serializable")]

        self.class_map[clazz.name] = clazz
        return clazz


