#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame

class ANEW_ARRAY(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        class_ref = rt_constant_pool.get_constant(self.index)
        component_class = class_ref.resolved_class()

        stack = frame.operand_stack
        count = stack.pop_numeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        array_class = component_class.array_class()
        array = array_class.new_array(count)
        stack.push_ref(array)



