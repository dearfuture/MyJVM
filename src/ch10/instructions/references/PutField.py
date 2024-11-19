#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame

class PUT_FIELD(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        field_ref = rt_constant_pool.get_constant(self.index)
        field = field_ref.resolved_field()
        clazz = field.get_class()

        if field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")
        if field.is_final():
            if current_class != clazz or current_method.name != "<init>":
                raise RuntimeError("java.lang.IllegalAccessError")

        descriptor = field.descriptor
        slot_id = field.slot_id
        stack = frame.operand_stack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "J"}:
            val = stack.pop_numeric()
            ref = stack.pop_ref()
            if ref is None:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.set_numeric(slot_id, val)

        if descriptor[0] == 'D':
            val = stack.pop_double()
            ref = stack.pop_ref()
            if ref is None:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.set_double(slot_id, val)
        if descriptor[0] == 'F':
            val = stack.pop_float()
            ref = stack.pop_ref()
            if ref is None:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.set_float(slot_id, val)

        elif descriptor[0] in {"L", "["}:
            val = stack.pop_ref()
            ref = stack.pop_ref()
            if ref is None:
                raise RuntimeError("java.lang.NullPointerException")
            ref.fields.set_ref(slot_id, val)







