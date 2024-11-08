#!/usr/bin/env python
# encoding: utf-8
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool
from classfile.ConstantInfo import ConstantInfo

class ConstantNameAndTypeInfo(ConstantInfo):
    constant_pool: ConstantPool
    # u2
    name_index = 0
    # u2
    descriptor_index = 0

    def __init__(self, constant_pool: ConstantPool):
        self.constant_pool = constant_pool

    def read_info(self, class_reader: ClassReader):
        # 第一次寻址获得name_index
        self.name_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        self.descriptor_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")