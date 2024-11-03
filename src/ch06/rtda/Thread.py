#!/usr/bin/env python
# encoding: utf-8

from rtda.Stack import Stack
from rtda.heap.Method import Method


class Thread:
    pc: int
    stack: Stack

    def __init__(self):
        self.pc = 0
        self.stack = Stack(1024)

    def push_frame(self, frame):
        self.stack.push(frame)

    def pop_frame(self):
        return self.stack.pop()

    @property
    def current_frame(self):
        return self.stack.top()

    # def new_frame(self, max_locals, max_stack):
    #     from .Frame import Frame
    #     return Frame(self, max_locals, max_stack)

    def new_frame(self, method: Method):
        from rtda.Frame import Frame
        return Frame(self, method)

    def is_stack_empty(self):
        return self.stack.is_empty()

    # 清空stack
    def clear_stack(self):
        self.stack.clear()