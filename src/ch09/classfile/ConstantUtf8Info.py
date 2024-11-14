#!/usr/bin/env python
# encoding: utf-8
from classfile.ClassReader import ClassReader
from classfile.ConstantInfo import ConstantInfo

# 字面量 Utf8String

class ConstantUtf8Info(ConstantInfo):
    # u2
    length = 0
    # u1
    bytes_data: bytes

    #转换bytes_data为可读字符串，从MUTF-8转换
    str = ""

    def __init__(self):
        self.str = ""

    @staticmethod
    def decode_mutf8(bytes_data):
        return bytes_data.decode()

    def read_info(self, class_reader: ClassReader):
        self.length = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        if self.length == 0:
            self.str = ""
        else:
            bytes_data = class_reader.read_bytes(self.length)
            self.str = self.decode_mutf8(bytes_data)