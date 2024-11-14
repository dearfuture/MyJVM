#!/usr/bin/env python
# encoding: utf-8
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool
from classfile.ConstantInfo import ConstantInfo

# ConstantFieldRefInfo, ConstantMethodRefInfo, ConstantInterfaceMethodRefInfo 的父类
class ConstantMemberRefInfo(ConstantInfo):
    constant_pool: ConstantPool

    # u2
    class_index = 0
    # u2
    name_type_index = 0

    def __init__(self, constant_pool: ConstantPool):
        self.constant_pool = constant_pool
        self.class_index = 0
        self.name_type_index = 0

    def read_info(self, class_reader: ClassReader):
        # index of ConstantClassInfo
        self.class_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        # index of ConstantNameAndTypeInfo
        self.name_type_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")

    @property
    def class_name(self):
        return self.constant_pool.get_class_name(self.class_index)

    @property
    def name_and_type(self):
        return self.constant_pool.get_name_and_type(self.name_type_index)

class ConstantFieldRefInfo(ConstantMemberRefInfo):
    def __init__(self, constant_pool: ConstantPool):
        super(ConstantFieldRefInfo, self).__init__(constant_pool)

class ConstantMethodRefInfo(ConstantMemberRefInfo):
    def __init__(self, constant_pool: ConstantPool):
        super(ConstantMethodRefInfo, self).__init__(constant_pool)

class ConstantInterfaceMethodRefInfo(ConstantMemberRefInfo):
    def __init__(self, constant_pool: ConstantPool):
        super(ConstantInterfaceMethodRefInfo, self).__init__(constant_pool)