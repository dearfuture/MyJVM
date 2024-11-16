#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Instruction, Index8Instruction, NoOperandsInstruction
from rtda.Frame import Frame


def _xload(frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_numeric()
    array_ref = stack.pop_ref()

    if array_ref is None:
        raise RuntimeError("java.lang.NullPointerException")
    xarray = array_ref.data

    if index < 0 or index >= len(xarray):
        raise RuntimeError("ArrayIndexOutOfBoundsException")
    stack.push_numeric(xarray[index])

# 非原生数组
class AALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        array_ref = stack.pop_ref()

        if array_ref is None:
            raise RuntimeError("java.lang.NullPointerException")
        refs = array_ref.refs

        if index < 0 or index >= len(refs):
            raise RuntimeError("ArrayIndexOutOfBoundsException")

        stack.push_ref(refs[index])

# Byte数组
class BALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xload(frame)

# Char数组
class CALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xload(frame)

# Double数组
class DALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        array_ref = stack.pop_ref()

        if array_ref is None:
            raise RuntimeError("java.lang.NullPointerException")
        xarray = array_ref.data

        if index < 0 or index >= len(xarray):
            raise RuntimeError("ArrayIndexOutOfBoundsException")
        stack.push_double(xarray[index])

# Float数组
class FALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        array_ref = stack.pop_ref()

        if array_ref is None:
            raise RuntimeError("java.lang.NullPointerException")
        xarray = array_ref.data

        if index < 0 or index >= len(xarray):
            raise RuntimeError("ArrayIndexOutOfBoundsException")
        stack.push_float(xarray[index])

# Integer数组
class IALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xload(frame)

# Long数组
class LALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xload(frame)

# Short数组
class SALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _xload(frame)
