#!/usr/bin/env python
# encoding: utf-8
from classfile.ClassFile import ClassFile
from rtda.Slot import Slots
from rtda.heap import AccessFlags
from rtda.heap.ClassNameHelper import ClassNameHelper
from rtda.heap.Field import Field
from rtda.heap.Method import Method
from rtda.heap.RuntimeConstantPool import RuntimeConstantPool

class Class:
    def __init__(self):
        # 访问标志
        self.access_flags = 0
        # 类名（完全限定名），具有java/lang/Object的形式
        self.name = ""
        # 超类名（完全限定名）
        self.super_class_name = ""
        # 接口名（完全限定名）
        self.interface_names = []
        # 运行时常量池指针
        self.rt_constant_pool = None
        # 字段表
        self.fields = []
        # 方法表
        self.methods = []
        # 加载器
        self.loader = None
        # 超类
        self.super_class = None
        # 接口
        self.interfaces = []
        # 实例变量所占空间
        self.instance_slot_count = 0
        # 类变量所占空间
        self.static_slot_count = 1
        # 静态变量
        self.static_vars = Slots()

        # ch07 类是否已经初始化(没有则可能触发<clinit>的调用)
        self.init_started = False

    @staticmethod
    def new_class(class_file: ClassFile):
        clazz = Class()
        clazz.access_flags = class_file.access_flags
        clazz.name = class_file.class_name
        clazz.super_class_name = class_file.super_class_name
        clazz.interface_names = class_file.interface_names

        # 不是直接调用RuntimeConstantPool()
        clazz.rt_constant_pool = RuntimeConstantPool.new_rt_constant_pool(clazz, class_file.constant_pool)

        # 填充成员和方法！！！
        clazz.fields = Field.new_fields(clazz, class_file.fields)
        clazz.methods = Method.new_methods(clazz, class_file.methods)

        return clazz

    def is_accessible_to(self, other):
        return self.is_public() or self.get_package_name() == other.get_package_name()

    def get_package_name(self):
        index = self.name.rfind("/")
        if index != -1:
            return self.name[:index]
        return ""

    # 用于判断public访问标志是否被设置
    def is_public(self):
        return 0 != self.access_flags & AccessFlags.ACC_PUBLIC
        # 判断S是否是T的超类

    def is_super_class_of(self, otherClass):
        return otherClass.is_sub_class_of(self)

    # 判断S是否是T的子类，也就是判断T是否是S的（直接或间接）超类
    def is_sub_class_of(self, other_class):
        c = self.super_class
        while c:
            if c == other_class:
                return True
            c = c.super_class

        return False

    # 获取main方法
    def get_main_method(self):
        return self.get_static_method("main", "([Ljava/lang/String;)V")

    def get_clinit_method(self):
        return self.get_static_method("<clinit>", "()V")

    def get_static_method(self, name: str, descriptor: str):
        for method in self.methods:
            if method.is_static() and method.name == name and method.descriptor == descriptor:
                return method
        return None

    def new_object(self):
        from .Object import Object
        return Object(self)

    # 用于判断super访问标志是否被设置
    def is_super(self):
        return 0 != self.access_flags & AccessFlags.ACC_SUPER

    # 用于判断interface访问标志是否被设置
    def is_interface(self):
        return 0 != self.access_flags & AccessFlags.ACC_INTERFACE

    # 判断S是否实现了T接口
    def is_implements(self, iface):
        c = self
        while c:
            for interface in c.interfaces:
                if interface == iface or interface.is_sub_interface_of(iface):
                    return True

        return False

    # 用于判断abstract访问标志是否被设置
    def is_abstract(self):
        return 0 != self.access_flags & AccessFlags.ACC_ABSTRACT

    def is_assignable_from(self, other_class):
        if self == other_class:
            return True
        if not self.is_interface():
            return other_class.is_sub_class_of(self)
        else:
            return other_class.is_implementation_of(self)

    def __str__(self):
        return "class name: ".join(self.name)


    # 数组类
    def is_array(self):
        return self.name[0] == '['

    def new_array(self, count):
        from .Object import Object
        if not self.is_array():
            raise RuntimeError("Not array class: {}".format(self.name))

        return Object(self, [0 for _ in range(count)])

    def array_class(self):
        array_class_name = ClassNameHelper.get_array_class_name(self.name)
        return self.loader.load_class(array_class_name)

