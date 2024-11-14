#!/usr/bin/env python
# encoding: utf-8
from classfile.AttributeInfo import AttributeInfo
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool

class ConstantValueAttribute(AttributeInfo):

    constant_pool:  ConstantPool
    # u2
    constant_value_index = 0

    def __init__(self, constant_pool: ConstantPool):
        self.constant_pool = constant_pool
        self.constant_value_index = 0

    def read_info(self, class_reader: ClassReader):
        self.constant_value_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")
