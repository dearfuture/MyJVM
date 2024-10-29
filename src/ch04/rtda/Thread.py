#!/usr/bin/env python
# encoding: utf-8

from rtda.Stack import Stack

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

    def current_frame(self):
        return self.stack.top()

