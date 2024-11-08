#!/usr/bin/env python
# encoding: utf-8
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

    # def set_numeric32(self, index, val):
    #     self.slots[index].num = val
    #
    # def get_numeric32(self, index):
    #     return self.slots[index].num
    #
    # def set_numeric64(self, index, val):
    #     self.slots[index].num = val
    #     self.slots[index + 1].num = 0
    #
    # def get_numeric64(self, index):
    #     return self.slots[index].num

    def set_ref(self, index, ref):
        self.slots[index].ref = ref

    def get_ref(self, index: int):
        return self.slots[index].ref

    def set_slot(self, index, slot):
        self.slots[index] = slot

    def __str__(self):
        return "slots:{0}".format([str(t) for t in self.slots])