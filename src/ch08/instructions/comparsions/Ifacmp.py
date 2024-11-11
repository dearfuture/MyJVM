#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction
from rtda.Frame import Frame

class IF_ACMPEQ(BranchInstruction):
    def execute(self, frame: Frame):
        ref2 = frame.operand_stack.pop_ref()
        ref1 = frame.operand_stack.pop_ref()
        if ref1 == ref2:
            branch(frame, self.offset)

class IF_ACMPNE(BranchInstruction):
    def execute(self, frame: Frame):
        ref2 = frame.operand_stack.pop_ref()
        ref1 = frame.operand_stack.pop_ref()
        if ref1 != ref2:
            branch(frame, self.offset)