#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Instruction, NoOperandsInstruction
from rtda.Frame import Frame


class IOR(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_numeric()
        v1 = frame.operand_stack.pop_numeric()
        result = v1 | v2
        frame.operand_stack.push_numeric(result)

class LOR(NoOperandsInstruction):
    def execute(self, frame: Frame):
        v2 = frame.operand_stack.pop_numeric()
        v1 = frame.operand_stack.pop_numeric()
        result = v1 | v2
        frame.operand_stack.push_numeric(result)