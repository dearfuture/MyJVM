#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


class DUP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        slot = frame.operand_stack.pop_slot()
        frame.operand_stack.push_slot(slot)
        frame.operand_stack.push_slot(slot)

