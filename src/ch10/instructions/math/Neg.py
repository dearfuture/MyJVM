#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


class INEG(NoOperandsInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        val = -val
        frame.operand_stack.push_numeric(val)

class LNEG(NoOperandsInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        val = -val
        frame.operand_stack.push_numeric(val)