#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Instruction, Index8Instruction, NoOperandsInstruction
from rtda.Frame import Frame


def _iload(frame: Frame, index: int):
    val = frame.local_vars.get_numeric(index)
    frame.operand_stack.push_numeric(val)

class ILOAD(Index8Instruction):
    def execute(self, frame: Frame):
        _iload(frame, self.index)

class ILOAD_0(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _iload(frame, 0)

class ILOAD_1(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _iload(frame, 1)

class ILOAD_2(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _iload(frame, 2)

class ILOAD_3(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _iload(frame, 3)