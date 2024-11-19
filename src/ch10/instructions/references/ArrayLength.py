#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame
from rtda.Slot import Slot

class ARRAY_LENGTH(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack

        # Object
        array_ref = stack.pop_ref()
        if array_ref is None:
            raise RuntimeError("java.lang.NullPointerException")
        array_length = array_ref.array_length()

        stack.push_numeric(array_length)