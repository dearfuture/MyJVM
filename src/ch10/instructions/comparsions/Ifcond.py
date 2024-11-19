#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import Instruction, BranchInstruction
from rtda.Frame import Frame


# ifeq: x == 0
class IFEQ(BranchInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        if 0 == val:
            branch(frame, self.offset)

# ifeq: x != 0
class IFNE(BranchInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        if 0 != val:
            branch(frame, self.offset)

# iflt: x < 0
class IFLT(BranchInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        if val < 0:
            branch(frame, self.offset)

# ifge: x >= 0
class IFGE(BranchInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        if val >= 0:
            branch(frame, self.offset)

# ifgt: x > 0
class IFGT(BranchInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        if val > 0:
            branch(frame, self.offset)

# ifle: x <= 0
class IFLE(BranchInstruction):
    def execute(self, frame: Frame):
        val = frame.operand_stack.pop_numeric()
        if val <= 0:
            branch(frame, self.offset)