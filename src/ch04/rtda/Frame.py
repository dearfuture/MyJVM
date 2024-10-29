#!/usr/bin/env python
# encoding: utf-8
from rtda.LocalVars import LocalVars
from rtda.OperandStack import OperandStack


class Frame:
    def __init__(self, max_locals, max_stack):
        self.lower = None
        self.local_vars = LocalVars(max_locals)
        self.operand_stack = OperandStack(max_stack)

