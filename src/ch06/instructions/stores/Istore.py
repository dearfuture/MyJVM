#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Instruction, Index8Instruction, NoOperandsInstruction
from rtda.Frame import Frame

def _istore(frame: Frame, index: int):
    val = frame.operand_stack.pop_numeric()
    frame.local_vars.set_numeric(index, val)

class ISTORE(Index8Instruction):
    def execute(self, frame: Frame):
        _istore(frame, self.index)

class ISTORE_0(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _istore(frame, 0)

class ISTORE_1(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _istore(frame, 1)

class ISTORE_2(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _istore(frame, 2)

class ISTORE_3(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _istore(frame, 3)