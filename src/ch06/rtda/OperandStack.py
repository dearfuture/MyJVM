#!/usr/bin/env python
# encoding: utf-8
from rtda.Slot import Slot


class OperandStack:
    # size用于定位栈顶
    size: int
    # slots: [Slot]
    slots: []

    def __init__(self, max_stack):
        self.slots = []
        if max_stack > 0:
            self.slots = [Slot() for _ in range(max_stack)]
        self.size = 0

    def push_numeric(self, val):
        self.slots[self.size].num = val
        self.size += 1

    def pop_numeric(self):
        self.size -= 1
        return self.slots[self.size].num

    # def push_numeric32(self, val):
    #     self.slots[self.size].num = val
    #     self.size += 1
    #
    # def pop_numeric32(self):
    #     self.size -= 1
    #     return self.slots[self.size].num
    #
    # def push_numeric64(self, val):
    #     self.slots[self.size].num = val
    #     self.size += 2
    #
    # def pop_numeric64(self):
    #     self.size -= 2
    #     return self.slots[self.size].num

    def push_ref(self, ref):
        self.slots[self.size].ref = ref
        self.size += 1

    # 因为Dup实现有问题的临时补丁, 已经不需要了
    # def pop_ref(self):
    #     self.size -= 1
    #     ref = self.slots[self.size].ref
    #     if self.size > 0:
    #         ref_bak = self.slots[self.size - 1].ref
    #     self.slots[self.size].ref = None
    #     if self.size > 0:
    #         self.slots[self.size - 1].ref = ref_bak
    #     return ref

    def pop_ref(self):
        self.size -= 1
        ref = self.slots[self.size].ref
        self.slots[self.size].ref = None
        return ref

    def push_slot(self, slot: Slot):
        self.slots[self.size] = slot
        self.size += 1

    def pop_slot(self):
        self.size -= 1
        return self.slots[self.size]

    def __str__(self):
        return "size:{0} slots:{1}".format(self.size, [str(t) for t in self.slots])