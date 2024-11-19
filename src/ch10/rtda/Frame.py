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

    # 重置next_pc为当前执行的虚拟机指令(如NEW/INVOKE_STATIC/GET_STATIC等), 用于被类加载打断, 执行<cinit>初始化后, 重新执行这条被打断的虚拟机指令
    def revert_next_pc(self):
        self.next_pc = self.thread.pc

