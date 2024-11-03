#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame

class IINC(Instruction):
    def __init__(self):
        self.index = 0
        self.const = 0

    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.index = bytecode_reader.read_uint8()
        self.const = bytecode_reader.read_int8()

    def execute(self, frame):
        local_vars = frame.local_vars
        val = local_vars.get_numeric(self.index)
        val += self.const
        local_vars.set_numeric(self.index, val)

