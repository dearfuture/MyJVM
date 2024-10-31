#!/usr/bin/env python
# encoding: utf-8
from rtda.LocalVars import LocalVars
from rtda.OperandStack import OperandStack
from rtda.Thread import Thread


class Frame:
    def __init__(self, thread: Thread, max_locals, max_stack):
        self.thread = thread
        self.next_pc = 0

        self.lower = None
        self.local_vars = LocalVars(max_locals)
        self.operand_stack = OperandStack(max_stack)


