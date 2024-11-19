#!/usr/bin/env python
# encoding: utf-8
import ctypes

class BytecodeReader:
    code: []
    pc: int

    def __init__(self):
        self.code = []
        self.pc = 0

    def reset(self, code, pc):
        self.code = code
        self.pc = pc

    def read_uint8(self):
        i = self.code[self.pc]
        self.pc += 1
        return ctypes.c_uint8(i).value

    def read_int8(self):
        i = self.code[self.pc]
        self.pc += 1
        return ctypes.c_int8(i).value

    def read_uint16(self):
        byte1 = self.read_uint8()
        byte2 = self.read_uint8()
        return ctypes.c_uint16( (byte1 << 8) | byte2 ).value

    def read_int16(self):
        return ctypes.c_int16( self.read_uint16() ).value

    def read_int32(self):
        byte1 = self.read_int8()
        byte2 = self.read_int8()
        byte3 = self.read_int8()
        byte4 = self.read_int8()
        return ctypes.c_int32( (byte1 << 24) | (byte2 << 16) | (byte3 << 8) | byte4).value

    def read_int32s(self, n):
        ints = []
        for i in range(n):
            ints.append(self.read_int32())
        return ints

    def skip_padding(self):
        while self.pc % 4 != 0:
            self.read_uint8()
