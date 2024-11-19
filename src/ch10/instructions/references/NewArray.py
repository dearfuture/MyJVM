#!/usr/bin/env python
# encoding: utf-8
from instructions.base import ClassInitLogic
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame

class NEW_ARRAY(Instruction):
    AT_BOOLEAN = 4
    AT_CHAR = 5
    AT_FLOAT = 6
    AT_DOUBLE = 7
    AT_BYTE = 8
    AT_SHORT = 9
    AT_INT = 10
    AT_LONG = 11

    def __init__(self):
        self.atype = 0

    def fetch_operands(self, reader):
        self.atype = reader.read_uint8()

    def execute(self, frame: Frame):
        stack = frame.operand_stack
        count = stack.pop_numeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        class_loader = frame.method.get_class().loader
        array_class = NEW_ARRAY.get_primitive_array_class(class_loader, self.atype)
        array = array_class.new_array(count)
        stack.push_ref(array)

    @staticmethod
    def get_primitive_array_class(class_loader, atype):
        if atype == NEW_ARRAY.AT_BOOLEAN:
            return class_loader.load_class("[Z")
        elif atype == NEW_ARRAY.AT_CHAR:
            return class_loader.load_class("[C")
        elif atype == NEW_ARRAY.AT_FLOAT:
            return class_loader.load_class("[F")
        elif atype == NEW_ARRAY.AT_DOUBLE:
            return class_loader.load_class("[D")
        elif atype == NEW_ARRAY.AT_BYTE:
            return class_loader.load_class("[B")
        elif atype == NEW_ARRAY.AT_SHORT:
            return class_loader.load_class("[S")
        elif atype == NEW_ARRAY.AT_INT:
            return class_loader.load_class("[I")
        elif atype == NEW_ARRAY.AT_LONG:
            return class_loader.load_class("[J")

        else:
            raise RuntimeError("Invalid atype!")
