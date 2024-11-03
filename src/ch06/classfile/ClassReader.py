#!/usr/bin/env python
# encoding: utf-8

class ClassReader:
    data: bytes
    index = 0

    def __init__(self, class_data: bytes):
        # byte[]
        self.data = class_data
        self.index = 0

    # u1
    def read_uint8(self):
        val = self.data[:1]
        self.data = self.data[1:]

        self.index += 1

        return val
    # u2
    def read_uint16(self):
        val = self.data[:2]
        self.data = self.data[2:]

        self.index += 2

        return val

    # u4
    def read_uint32(self):
        val = self.data[:4]
        self.data = self.data[4:]

        self.index += 4

        return val

    # u8
    def read_uint64(self):
        val = self.data[:8]
        self.data = self.data[8:]

        self.index += 8

        return val

    # {n, u2[]}，一般用于读取interfaces, exceptions等
    def read_uint16s(self):
        # 读取n个u2
        n = int.from_bytes(self.read_uint16(), byteorder="big")
        s = []
        for i in range(n):
            s.append(int.from_bytes(self.read_uint16(), byteorder="big"))

        self.index += n

        return s

    # 读取指定数量的字节，一般用于读取Uft8String
    def read_bytes(self, n):
        bytes_data = self.data[:n]
        self.data = self.data[n:]

        self.index += n

        return bytearray(bytes_data)
