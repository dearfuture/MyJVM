#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index16Instruction


class CHECK_CAST(Index16Instruction):
    def execute(self, frame):
        stack = frame.operand_stack
        ref = stack.pop_ref()
        # 与INSTANCE_OF的区别1：会压栈回去
        stack.push_ref(ref)
        if ref is None:
            # False
            stack.push_numeric(0)
            return

        rt_constant_pool = frame.method.get_class().rt_constant_pool
        class_ref = rt_constant_pool.get_constant(self.index)
        clazz = class_ref.resolved_class()
        if not ref.is_instance_of(clazz):
            # 与INSTANCE_OF的区别2：检查不通过直接弹出异常
            raise RuntimeError("java.lang.ClassCastException")