#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Instruction, NoOperandsInstruction
from rtda.Frame import Frame


class IMUL(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_numeric()
        v1 = frame.operand_stack.pop_numeric()
        result = v1 * v2
        frame.operand_stack.push_numeric(result)

class LMUL(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_numeric()
        v1 = frame.operand_stack.pop_numeric()
        result = v1 * v2
        frame.operand_stack.push_numeric(result)

class FMUL(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_float()
        v1 = frame.operand_stack.pop_float()
        result = v1 * v2
        frame.operand_stack.push_float(result)

class DMUL(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_double()
        v1 = frame.operand_stack.pop_double()
        result = v1 * v2
        frame.operand_stack.push_double(result)