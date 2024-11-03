#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Instruction, Index8Instruction, NoOperandsInstruction
from rtda.Frame import Frame


def _aload(frame: Frame, index: int):
    ref = frame.local_vars.get_ref(index)
    frame.operand_stack.push_ref(ref)

class ALOAD(Index8Instruction):
    def execute(self, frame: Frame):
        _aload(frame, self.index)

class ALOAD_0(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _aload(frame, 0)

class ALOAD_1(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _aload(frame, 1)

class ALOAD_2(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _aload(frame, 2)

class ALOAD_3(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _aload(frame, 3)