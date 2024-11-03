#!/usr/bin/env python
# encoding: utf-8
from rtda.Slot import Slots


class Object:
    def __init__(self, clazz):
        self.clazz = clazz
        # 占位，后续用于存放field (PUT_FIELD)
        self.fields = Slots(clazz.instance_slot_count)

    def is_instance_of(self, clazz):
        return clazz.is_assignable_from(self.clazz)
