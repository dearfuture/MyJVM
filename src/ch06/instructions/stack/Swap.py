#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


class SWAP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        slot1 = frame.operand_stack.pop_slot()
        slot2 = frame.operand_stack.pop_slot()
        frame.operand_stack.push_slot(slot1)
        frame.operand_stack.push_slot(slot2)

