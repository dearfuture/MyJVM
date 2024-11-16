#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame
from rtda.Slot import copy_slot


class DUP(NoOperandsInstruction):
    def execute(self, frame: Frame):
        slot = frame.operand_stack.pop_slot()
        frame.operand_stack.push_slot(slot)

        frame.operand_stack.push_slot(copy_slot(slot))

class DUP_X1(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
              __/
             |
             V
    [...][c][a][b][a]
    """

    def execute(self, frame):
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(copy_slot(slot1))
        stack.push_slot(slot2)
        stack.push_slot(slot1)


class DUP_X2(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
           _____/
          |
          V
    [...][a][c][b][a]
    """

    def execute(self, frame):
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(copy_slot(slot1))
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)

class DUP2(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]____
              \____   |
                   |  |
                   V  V
    [...][c][b][a][b][a]
    """

    def execute(self, frame):
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot2)
        stack.push_slot(slot1)
        stack.push_slot(copy_slot(slot2))
        stack.push_slot(copy_slot(slot1))

class DUP2_X1(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
           _/ __/
          |  |
          V  V
    [...][b][a][c][b][a]
    """

    def execute(self, frame):
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(copy_slot(slot2))
        stack.push_slot(copy_slot(slot1))
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)


class DUP2_X2(NoOperandsInstruction):
    """
    bottom -> top
    [...][d][c][b][a]
           ____/ __/
          |   __/
          V  V
    [...][b][a][d][c][b][a]
    """

    def execute(self, frame):
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        slot4 = stack.pop_slot()
        stack.push_slot(copy_slot(slot2))
        stack.push_slot(copy_slot(slot1))
        stack.push_slot(slot4)
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)
