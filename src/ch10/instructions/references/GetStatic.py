#!/usr/bin/env python
# encoding: utf-8
from instructions.base import ClassInitLogic
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class GET_STATIC(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        field_ref = rt_constant_pool.get_constant(self.index)
        field = field_ref.resolved_field()
        clazz = field.get_class()

        if not clazz.init_started:
            # 重置next_pc, 执行完init_class即<clinit>后再重新执行NEW
            frame.revert_next_pc()
            ClassInitLogic.init_class(frame.thread, clazz)
            return

        if not field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        descriptor = field.descriptor
        slot_id = field.slot_id
        slots = clazz.static_vars
        stack = frame.operand_stack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "J"}:
            stack.push_numeric(slots.get_numeric(slot_id))

        elif descriptor[0] == 'F':
            stack.push_float(slots.get_float(slot_id))
        elif descriptor[0] == 'D':
            stack.push_double(slots.get_double(slot_id))

        elif descriptor[0] in {"L", "["}:
            stack.push_ref(slots.get_ref(slot_id))







