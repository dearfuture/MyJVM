#!/usr/bin/env python
# encoding: utf-8
import struct


class Slot:
    # 存放数字
    # num: int/float/long/double
    # 存放引用
    # ref: Object

    def __init__(self):
        self.num = 0
        self.ref = None

    def __str__(self):
        return "num:{0} ref:{1}".format(self.num, self.ref)

class Slots(list):
    def __init__(self, slot_count = 1):
        super().__init__([Slot() for _ in range(slot_count)])

    def set_numeric(self, index, val):
        self[index].num = val

    def get_numeric(self, index):
        return self[index].num

    def set_double(self, index, val):
        val = struct.unpack('>q', struct.pack('>d', val))[0]
        self.set_numeric(index, val)

    def get_double(self, index):
        val = self.get_numeric(index)
        return struct.unpack('>d', struct.pack('>q', val))[0]

    def set_float(self, index, val):
        val = struct.unpack('>l', struct.pack('>f', val))[0]
        self.set_numeric(index, val)

    def get_float(self, index):
        val = self.get_numeric(index)
        return struct.unpack('>f', struct.pack('>l', val))[0]

    def set_ref(self, index, ref):
        self[index].ref = ref

    def get_ref(self, index):
        return self[index].ref