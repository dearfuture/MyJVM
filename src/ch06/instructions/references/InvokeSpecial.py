#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame: Frame):
        # HACK
        frame.operand_stack.pop_ref()