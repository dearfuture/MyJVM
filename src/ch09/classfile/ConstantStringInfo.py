#!/usr/bin/env python
# encoding: utf-8
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool
from classfile.ConstantInfo import ConstantInfo


class ConstantStringInfo(ConstantInfo):
    constant_pool: ConstantPool

    # u2
    string_index = 0

    def __init__(self, constant_pool: ConstantPool):
        self.constant_pool = constant_pool

    def  read_info(self, class_reader: ClassReader):
        #第一次寻址获得string_index
        self.string_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")

    def __str__(self):
        #第二次寻址获得constant_pool[string_index]对应的Utf8String
        return self.constant_pool.get_utf8_str(self.string_index)

