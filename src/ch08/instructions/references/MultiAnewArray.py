#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame

def pop_and_check_counts(stack, dimensions):
    counts = [0 for _ in range(dimensions)]
    i = dimensions - 1
    while i >= 0:
        counts[i] = stack.pop_numeric()
        if counts[i] < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")
        i -= 1
    return counts

def new_multi_dimensional_array(counts, array_class):
    count = counts[0]
    array = array_class.new_array(count)

    if len(counts) > 1:
        refs = array.refs
        for i in range(len(refs)):
            refs[i] = new_multi_dimensional_array(counts[1:], array_class.component_class())

    return array


class MULTI_ANEW_ARRAY(NoOperandsInstruction):
    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.index = bytecode_reader.read_uint16()
        self.dimensions = bytecode_reader.read_uint8()

    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        class_ref = rt_constant_pool.get_constant(self.index)
        array_class = class_ref.resolved_class()

        stack = frame.operand_stack
        counts = pop_and_check_counts(stack, self.dimensions)
        array = new_multi_dimensional_array(counts, array_class)
        stack.push_ref(array)



