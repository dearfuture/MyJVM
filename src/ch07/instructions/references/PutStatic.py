#!/usr/bin/env python
# encoding: utf-8
from instructions.base import ClassInitLogic
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame

class PUT_STATIC(Index16Instruction):
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
        if field.is_final():
            if current_class != clazz or current_method.name != "<clinit>":
                raise RuntimeError("java.lang.IllegalAccessError")

        descriptor = field.descriptor
        slot_id = field.slot_id
        slots = clazz.static_vars
        stack = frame.operand_stack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "J"}:
            slots.set_numeric(slot_id, stack.pop_numeric())
        elif descriptor[0] in {"F", "D"}:
            slots.set_numeric(slot_id, stack.pop_numeric())
        elif descriptor[0] in {"L", "["}:
            slots.set_ref(slot_id, stack.pop_ref())







