#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index16Instruction
from instructions.base.MethodInvokeLogic import invoke_method
from rtda.Frame import Frame


class INVOKE_STATIC(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        method_ref = rt_constant_pool.get_constant(self.index)

        resolved_method = method_ref.resolved_method()

        if not resolved_method.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        invoke_method(frame, resolved_method)

