#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame
from rtda.Slot import Slot


def copy_slot(slot):
    new_slot = Slot()
    new_slot.num = slot.num
    new_slot.ref = slot.ref
    return new_slot

class DUP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        slot = frame.operand_stack.pop_slot()
        frame.operand_stack.push_slot(slot)

        # Fix: 不能直接push(slot)也不能调用push(slot.copy()), 必须手动实现拷贝slot再push
        # 直接push(slot)会导致改变"栈顶"slots[index]的同时改变"次栈顶"slots[index-1]
        # 不能调用push(slot.copy())，因为ref直接值拷贝即可，不要slot.copy()这种深拷贝
        frame.operand_stack.push_slot(copy_slot(slot))


