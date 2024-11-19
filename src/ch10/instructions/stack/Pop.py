#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


class POP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        frame.operand_stack.pop_slot()

# 本来用于pop long/double(占据2个slot), 但由于本虚拟机的实现long/double只占据一个slot，所以只pop一次
class POP2(NoOperandsInstruction):
    def execute(self, frame: Frame):
        frame.operand_stack.pop_slot()
        # 本虚拟机的POP2也只进行一次pop
        # frame.operand_stack.pop_slot()