#!/usr/bin/env python
# encoding: utf-8
import struct

from rtda.Slot import Slot


class LocalVars:
    max_locals: int
    slots: [Slot]

    def __init__(self, max_locals):
        self.slots = []
        if max_locals > 0:
            # max_locals占位
            self.slots = [Slot() for _ in range(max_locals)]

    def set_numeric(self, index, val):
        self.slots[index].num = val

    def get_numeric(self, index):
        return self.slots[index].num

    def get_double(self, index):
        val = self.get_numeric(index)
        return struct.unpack('>d', struct.pack('>q', val))[0]

    def set_double(self, index, val):
        val = struct.unpack('>q', struct.pack('>d', val))[0]
        self.set_numeric(index, val)

    def get_float(self, index):
        val = self.get_numeric(index)
        return struct.unpack('>f', struct.pack('>l', val))[0]

    def set_float(self, index, val):
        val = struct.unpack('>l', struct.pack('>f', val))[0]
        self.set_numeric(index, val)

    def set_ref(self, index, ref):
        self.slots[index].ref = ref

    def get_ref(self, index: int):
        return self.slots[index].ref

    def set_slot(self, index, slot):
        self.slots[index] = slot

    def __str__(self):
        return "slots:{0}".format([str(t) for t in self.slots])