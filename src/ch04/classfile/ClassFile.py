#!/usr/bin/env python
# encoding: utf-8
from classfile.AttributeInfo import AttributeInfo
from classfile.MemberInfo import MemberInfo
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool

class ClassFile:

    # big-endian存储
    # 凡是index, length都是u2，标准处理int.from_bytes(class_reader.read_uint16(), byteorder="big")
    # tag都是u1

    constant_pool: ConstantPool
    access_flags: int
    this_class: int
    super_class: int
    interfaces: [int]

    def __init__(self):
        # 魔数
        self.magic = ""
        # 小版本号
        self.minor_version = ""
        # 主版本号
        self.major_version = ""
        # 常量池
        # self.constant_pool = None
        # 类访问标志，用于指出class文件定义的是类还是接口，访问级别是public还是private
        self.access_flags = 0
        # 类索引
        self.this_class = 0
        # 超类索引
        self.super_class = 0
        # 接口索引表
        self.interfaces = []
        # 变量
        self.fields = []
        # 方法
        self.methods = []
        # 属性
        self.attributes = []

    @staticmethod
    def parse(class_data):
        cr = ClassReader(class_data)
        cf = ClassFile()
        cf.read(cr)
        return cf

    def read(self, class_reader: ClassReader):
        self.read_and_check_magic(class_reader)
        self.read_and_check_version(class_reader)

        self.constant_pool = ConstantPool()
        self.constant_pool.read_constant_pool(class_reader)

        self.access_flags = int.from_bytes(class_reader.read_uint16(), byteorder="big")

        self.this_class = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        self.super_class = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        self.interfaces = class_reader.read_uint16s()

        self.fields = MemberInfo.read_members(class_reader, self.constant_pool)
        self.methods = MemberInfo.read_members(class_reader, self.constant_pool)
        self.attributes = AttributeInfo.read_attributes(class_reader, self.constant_pool)


    def read_and_check_magic(self, class_reader: ClassReader):
        magic = class_reader.read_uint32()
        self.magic = magic

        if magic != b'\xca\xfe\xba\xbe':
            raise RuntimeError("java.lang.ClassFormatError: magic!")

    def read_and_check_version(self, class_reader: ClassReader):
        self.minor_version = int.from_bytes(class_reader.read_uint16(), byteorder='big')
        self.major_version = int.from_bytes(class_reader.read_uint16(), byteorder='big')


    @property
    def class_name(self):
        return self.constant_pool.get_class_name(self.this_class)

    @property
    def super_class_name(self):
        if self.super_class:
            return self.constant_pool.get_class_name(self.super_class)
        # java.lang.Object...
        return ""

    @property
    def interface_names(self):
        ret = []
        for index in self.interfaces:
            ret.append(self.constant_pool.get_class_name(index))
        return ret
