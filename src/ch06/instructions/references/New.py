#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame

class NEW(Index16Instruction):
    def execute(self, frame: Frame):
        rt_constant_pool = frame.method.get_class().rt_constant_pool
        class_ref = rt_constant_pool.get_constant(self.index)
        clazz = class_ref.resolved_class()

        if clazz.is_interface() or clazz.is_abstract():
            raise RuntimeError("java.lang.InstantiationError")

        # 生成对象并返回对象的ref，压入堆栈
        ref = clazz.new_object()
        frame.operand_stack.push_ref(ref)

