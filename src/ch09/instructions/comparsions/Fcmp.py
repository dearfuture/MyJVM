#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction, NoOperandsInstruction
from rtda.Frame import Frame


class FCMPL(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        v2 = stack.pop_float()
        v1 = stack.pop_float()
        if v1 > v2:
            stack.push_numeric(1)
        elif v1 == v2:
            stack.push_numeric(0)
        elif v1 < v2:
            stack.push_numeric(-1)
        else:
            stack.push_numeric(1)

class FCMPG(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        v2 = stack.pop_float()
        v1 = stack.pop_float()
        if v1 > v2:
            stack.push_numeric(1)
        elif v1 == v2:
            stack.push_numeric(0)
        elif v1 < v2:
            stack.push_numeric(-1)
        else:
            stack.push_numeric(-1)