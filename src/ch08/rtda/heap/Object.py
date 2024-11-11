#!/usr/bin/env python
# encoding: utf-8
from rtda.Slot import Slots
from rtda.heap.Class import Class

# 实际上是ObjectRef, 与ClassRef, FieldRef, MethodRef之类的不同
class Object:
    def __init__(self, clazz: Class, data=None):
        self.clazz = clazz
        # 占位，后续用于存放field (PUT_FIELD)
        # self.fields = Slots(clazz.instance_slot_count)
        if data is None:
            self.data = []
        else:
            self.data = data

    @staticmethod
    def new_object(clazz: Class):
        return Object(clazz, Slots(clazz.instance_slot_count))

    def is_instance_of(self, clazz):
        return clazz.is_assignable_from(self.clazz)

    def get_class(self):
        return self.clazz

    @property
    def fields(self):
        return self.data

    # 引用类型数组
    @property
    def refs(self):
        return self.data

    @property
    def bytes(self):
        return self.data

    @property
    def shorts(self):
        return self.data

    @property
    def ints(self):
        return self.data

    @property
    def longs(self):
        return self.data

    @property
    def chars(self):
        return self.data

    @property
    def floats(self):
        return self.data

    @property
    def doubles(self):
        return self.data

    def array_length(self):
        return len(self.data)


