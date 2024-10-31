#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction
from rtda.Frame import Frame


class Goto(BranchInstruction):
    # 在BranchInstruction实现
    # def fetch_operands

    def execute(self, frame: Frame):
        branch(frame, self.offset)