#!/usr/bin/env python
# encoding: utf-8
import ctypes
import struct

from classfile.ClassReader import ClassReader
from classfile.ConstantInfo import ConstantInfo

# 字面量
# Integer Float Long Double
# Long和Double占2个数组位

class ConstantIntegerInfo(ConstantInfo):
    val: int

    def __init__(self):
        self.val = 0

    def read_info(self, class_reader: ClassReader):
        bytes_data = int.from_bytes(class_reader.read_uint32(), byteorder="big")
        self.val = ctypes.c_uint32(bytes_data).value

class ConstantFloatInfo(ConstantInfo):
    val: float

    def __init__(self):
        self.val = 0.0

    def read_info(self, class_reader: ClassReader):
        bytes_data = int.from_bytes(class_reader.read_uint32(), byteorder="big")
        self.val = struct.unpack('>f', struct.pack('>l', bytes_data))[0]

class ConstantLongInfo(ConstantInfo):
    val = 0

    def __init__(self):
        self.val = 0

    def read_info(self, class_reader: ClassReader):
        bytes_data = int.from_bytes(class_reader.read_uint64(), byteorder="big")
        self.val = ctypes.c_uint64(bytes_data).value

class ConstantDoubleInfo(ConstantInfo):
    val = 0.0

    def __init__(self):
        self.val = 0.0

    def read_info(self, class_reader: ClassReader):
        bytes_data = int.from_bytes(class_reader.read_uint64(), byteorder="big")
        self.val = struct.unpack('>d', struct.pack('>q', bytes_data))[0]