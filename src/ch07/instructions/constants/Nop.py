#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


class NOP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        pass