#!/usr/bin/env python
# encoding: utf-8
from instructions.base import ClassInitLogic
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

        clazz = resolved_method.get_class()
        if not clazz.init_started:
            # 重置next_pc, 执行完init_class即<clinit>后再重新执行NEW
            frame.revert_next_pc()
            ClassInitLogic.init_class(frame.thread, clazz)
            return

        if not resolved_method.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        invoke_method(frame, resolved_method)

