#!/usr/bin/env python
# encoding: utf-8
from rtda.LocalVars import LocalVars
from rtda.OperandStack import OperandStack
from rtda.Thread import Thread
from rtda.heap.Method import Method


class Frame:
    def __init__(self, thread: Thread, method: Method):
        # 用来实现链表数据结构
        self.lower = None
        self.thread = thread
        self.method = method
        # 保存局部变量表指针
        self.local_vars = LocalVars(method.max_locals)
        # 保存操作数栈指针
        self.operand_stack = OperandStack(method.max_stack)
        self.next_pc = 0


