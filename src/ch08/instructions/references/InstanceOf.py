#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index16Instruction

class INSTANCE_OF(Index16Instruction):
    def execute(self, frame):
        stack = frame.operand_stack
        ref = stack.pop_ref()
        if ref is None:
            # False
            stack.push_numeric(0)
            return

        rt_constant_pool = frame.method.get_class().rt_constant_pool
        class_ref = rt_constant_pool.get_constant(self.index)
        clazz = class_ref.resolved_class()
        if ref.is_instance_of(clazz):
            # True
            stack.push_numeric(1)
        else:
            # False
            stack.push_numeric(0)