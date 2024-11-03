#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame


class BIPUSH(Instruction):
    # int8
    val = 0

    def __init__(self):
        self.val = 0

    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.val = bytecode_reader.read_int8()

    def execute(self, frame: Frame):
        frame.operand_stack.push_numeric(self.val)


class SIPUSH(Instruction):
    # int8
    val = 0

    def __init__(self):
        self.val = 0

    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.val = bytecode_reader.read_int16()

    def execute(self, frame: Frame):
        frame.operand_stack.push_numeric(self.val)