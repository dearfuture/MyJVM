#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Instruction, Index8Instruction, NoOperandsInstruction
from rtda.Frame import Frame


def _fload(frame: Frame, index: int):
    val = frame.local_vars.get_float(index)
    frame.operand_stack.push_float(val)

class FLOAD(Index8Instruction):
    def execute(self, frame: Frame):
        _fload(frame, self.index)

class FLOAD_0(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _fload(frame, 0)

class FLOAD_1(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _fload(frame, 1)

class FLOAD_2(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _fload(frame, 2)

class FLOAD_3(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _fload(frame, 3)