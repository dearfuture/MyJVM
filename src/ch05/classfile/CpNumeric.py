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

# 使用4字节存储IEEE754单精度浮点数常量
class ConstantFloatInfo(ConstantInfo):
    def __init__(self):
        self.val = 0.0

    # 先读取一个uint32数据，然后把它转型成int32类型
    def read_info(self, class_reader):
        bytes_data = int.from_bytes(class_reader.read_uint32(), byteorder='big')
        self.val = struct.unpack('>f', struct.pack('>L', bytes_data))[0]

class ConstantLongInfo(ConstantInfo):
    val = 0

    def __init__(self):
        self.val = 0

    def read_info(self, class_reader: ClassReader):
        bytes_data = int.from_bytes(class_reader.read_uint64(), byteorder="big")
        self.val = ctypes.c_uint64(bytes_data).value

# 使用8字节存储IEEE754双精度浮点数
class ConstantDoubleInfo(ConstantInfo):
    def __init__(self):
        self.val = 0.0

    def read_info(self, class_reader):
        bytes_data = int.from_bytes(class_reader.read_uint64(), byteorder='big')
        self.val = struct.unpack('>d', struct.pack('>Q', bytes_data))[0]