#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


class IREM(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_numeric()
        v1 = frame.operand_stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticError: / by zero")
        result = v1 % v2
        frame.operand_stack.pop_numeric(result)

