#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction
from rtda.Frame import Frame


class IF_ICMPLE(BranchInstruction):
    def execute(self, frame: Frame):
        val2 = frame.operand_stack.pop_numeric()
        val1 = frame.operand_stack.pop_numeric()
        if val1 <= val2:
            branch(frame, self.offset)