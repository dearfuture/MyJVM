#!/usr/bin/env python
# encoding: utf-8
from classfile.AttributeInfo import AttributeInfo
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool

class SourceFileAttribute(AttributeInfo):

    constant_pool:  ConstantPool
    # u2
    source_file_index = 0

    def __init__(self, constant_pool: ConstantPool):
        self.constant_pool = constant_pool
        self.source_file_index = 0

    def read_info(self, class_reader: ClassReader):
        self.source_file_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")

    @property
    def file_name(self):
        return self.constant_pool.get_utf8_str(self.source_file_index)