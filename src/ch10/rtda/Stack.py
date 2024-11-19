#!/usr/bin/env python
# encoding: utf-8

class Stack:
    max_size: int
    size: int
    # __top: Frame

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        self.__top = None

    def push(self, frame):
        if self.size >= self.max_size:
            raise RuntimeError("java.lang.StackOverflowError")
        if self.__top:
            frame.lower = self.__top
        self.__top = frame
        self.size += 1

    def pop(self):
        if self.__top is None:
            raise RuntimeError("stack is empty")

        top = self.__top
        self.__top = top.lower
        top.lower = None
        self.size -= 1

        return top

    def top(self):
        if self.__top is None:
            raise RuntimeError("stack is empty")
        return self.__top

    def is_empty(self):
        return self.__top is None

    def clear(self):
        while not self.is_empty():
            self.pop()

    def get_frames(self):
        frames = []
        frame = self.__top
        while frame is not None:
            frames.append(frame)
            frame = frame.lower
        return frames