#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index8Instruction, Index16Instruction
from rtda.heap import StringPool
from rtda.heap.CpClassRef import ClassRef


def _ldc(frame, index):
    stack = frame.operand_stack
    rt_constant_pool = frame.method.get_class().rt_constant_pool
    c = rt_constant_pool.get_constant(index)
    clazz = frame.method.get_class()

    if isinstance(c, int):
        stack.push_numeric(c)

    elif isinstance(c, float):
        stack.push_float(c)

    #  elif cp_info.tag == ConstantInfo.CONSTANT_String:  consts[i] = str(cp_info)
    elif isinstance(c, str):
        interned_str = StringPool.j_string(clazz.loader, c)
        stack.push_ref(interned_str)

    #  elif cp_info.tag == ConstantInfo.CONSTANT_Class:  consts[i] = ClassRef.new_class_ref(rt_constant_pool, cp_info)
    elif isinstance(c, ClassRef):
        class_ref = c
        class_obj = class_ref.resolved_class().j_class
        stack.push_ref(class_obj)

    else:
        raise RuntimeError("java.lang.ClassFormatError")

class LDC(Index8Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)

class LDC_W(Index16Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)

class LDC2_W(Index16Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)