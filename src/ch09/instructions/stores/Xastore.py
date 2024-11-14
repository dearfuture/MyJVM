#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Instruction, Index8Instruction, NoOperandsInstruction
from rtda.Frame import Frame


def _xstore(frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_numeric()
    index = stack.pop_numeric()
    array_ref = stack.pop_ref()

    if array_ref is None:
        raise RuntimeError("java.lang.NullPointerException")
    xarray = array_ref.data

    if index < 0 or index >= len(xarray):
        raise RuntimeError("ArrayIndexOutOfBoundsException")
    xarray[index] = val

# 非原生数组
class AASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        ref = stack.pop_ref()
        index = stack.pop_numeric()
        array_ref = stack.pop_ref()

        if array_ref is None:
            raise RuntimeError("java.lang.NullPointerException")
        refs = array_ref.refs

        if index < 0 or index >= len(refs):
            raise RuntimeError("ArrayIndexOutOfBoundsException")

        refs[index] = ref

# Byte数组
class BASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)

# Char数组
class CASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)

# Double数组
class DASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)

# Float数组
class FASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)

# Integer数组
class IASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)

# Long数组
class LASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)

# Short数组
class SASTORE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xstore(frame)
