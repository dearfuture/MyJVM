#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class INVOKE_VIRTUAL(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        method_ref = rt_constant_pool.get_constant(self.index)

        # HACK!!!
        if method_ref.name == "println":
            stack = frame.operand_stack
            descriptor = method_ref.descriptor

            if descriptor == "(Z)V":
                print("{0}".format(stack.pop_numeric() != 0))
            elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V", "(F)V", "(D)V"}:
                print("{0}".format(stack.pop_numeric()))
            else:
                raise RuntimeError("println: " + method_ref.descriptor)

            # 人工ret
            stack.pop_ref()

