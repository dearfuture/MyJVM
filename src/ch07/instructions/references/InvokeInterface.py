#!/usr/bin/env python
# encoding: utf-8
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import Index16Instruction
from instructions.base.MethodInvokeLogic import invoke_method
from rtda.Frame import Frame
from rtda.heap.MethodLookup import lookup_method_in_class


class INVOKE_INTERFACE(Index16Instruction):
    def fetch_operands(self, bytecode_reader: BytecodeReader):
        self.index = bytecode_reader.read_uint16()
        # count
        bytecode_reader.read_uint8()
        # 必须为0
        bytecode_reader.read_uint8()

    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        method_ref = rt_constant_pool.get_constant(self.index)
        resolved_method = method_ref.resolved_interface_method()
        if resolved_method.static() or resolved_method.is_private():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        obj_ref = frame.operand_stack.get_ref_from_top(resolved_method.arg_slot_count - 1)
        if obj_ref is None:
            raise RuntimeError("java.lang.NullPointerException")
        if not obj_ref.get_class().is_implements(method_ref.resolved_class()):
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        method_to_be_invoked = lookup_method_in_class(obj_ref.get_class(), method_ref.name, method_ref.descriptor)

        if method_to_be_invoked is None or method_to_be_invoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")
        if not method_to_be_invoked.is_public():
            raise RuntimeError("java.lang.IllegalAccessError")

        invoke_method(frame, method_to_be_invoked)
