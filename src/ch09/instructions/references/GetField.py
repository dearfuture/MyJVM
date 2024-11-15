#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class GET_FIELD(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        field_ref = rt_constant_pool.get_constant(self.index)
        field = field_ref.resolved_field()
        clazz = field.get_class()

        if field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        stack = frame.operand_stack
        ref = stack.pop_ref()
        if ref is None:
            raise RuntimeError("java.lang.NullPointerException")

        descriptor = field.descriptor
        slot_id = field.slot_id
        slots = ref.fields

        if descriptor[0] in {"Z", "B", "C", "S", "I", "J"}:
            stack.push_numeric(slots.get_numeric(slot_id))

        elif descriptor[0] == 'F':
            stack.push_float(slots.get_float(slot_id))
        elif descriptor[0] == 'D':
            stack.push_double(slots.get_double(slot_id))

        elif descriptor[0] in {"L", "["}:
            stack.push_ref(slots.get_ref(slot_id))







