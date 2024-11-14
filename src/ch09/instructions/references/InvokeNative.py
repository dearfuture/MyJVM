#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from native import Registry
from rtda.Frame import Frame

class INVOKE_NATIVE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        method = frame.method
        class_name = method.get_class().name
        method_name = method.name
        method_descriptor = method.descriptor

        native_method = Registry.find_native_method(class_name, method_name, method_descriptor)
        if native_method is None:
            method_info = class_name + "." + method_name + method_descriptor
            raise RuntimeError("java.lang.UnsatisfiedLinkError: " + method_info)

        native_method(frame)