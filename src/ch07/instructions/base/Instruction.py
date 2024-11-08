#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod

from instructions.base.BytecodeReader import BytecodeReader
from rtda.Frame import Frame


class Instruction(metaclass=ABCMeta):

    # 从字节码中提取操作数
    @abstractmethod
    def fetch_operands(self, bytecode_reader: BytecodeReader):
        pass

    # 执行指令逻辑
    @abstractmethod
    def execute(self, frame: Frame):
        pass

# 表示没有操作数的指令
class NoOperandsInstruction(Instruction):
    def fetch_operands(self, bytecode_reader: BytecodeReader):
        pass

    def execute(self, frame: Frame):
        pass

class BranchInstruction(Instruction):
    def __init__(self):
        self.offset = 0

    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.offset = bytecode_reader.read_int16()

    def execute(self, frame: Frame):
        pass

class Index8Instruction(Instruction):
    def __init__(self):
        self.index = 0

    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.index = bytecode_reader.read_uint8()

    def execute(self, frame: Frame):
        pass

class Index16Instruction(Instruction):
    def __init__(self):
        self.index = 0

    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.index = bytecode_reader.read_uint16()

    def execute(self, frame: Frame):
        pass