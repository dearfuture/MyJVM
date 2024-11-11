#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction, NoOperandsInstruction
from rtda.Frame import Frame


class LCMP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v1 > v2:
            stack.push_numeric(1)
        elif v1 == v2:
            stack.push_numeric(0)
        else:
            stack.push_numeric(-1)