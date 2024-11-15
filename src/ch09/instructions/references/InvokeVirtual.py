#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import Index16Instruction
from instructions.base.MethodInvokeLogic import invoke_method
from rtda.Frame import Frame
from rtda.heap.MethodLookup import lookup_method_in_class
from rtda.heap import StringPool


class INVOKE_VIRTUAL(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        method_ref = rt_constant_pool.get_constant(self.index)
        resolved_method = method_ref.resolved_method()
        if resolved_method.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        obj_ref = frame.operand_stack.get_ref_from_top(resolved_method.arg_slot_count - 1)
        if obj_ref is None:

            # HACK!!!
            if method_ref.name == "println":
                print("--------------------println--------------------")
                stack = frame.operand_stack
                descriptor = method_ref.descriptor

                if descriptor == "(Z)V":
                    print("{0}".format(stack.pop_numeric() != 0))
                elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V"}:
                    print("{0}".format(stack.pop_numeric()))


                elif descriptor == "(D)V":
                    print("{0}".format(stack.pop_double()))
                elif descriptor == "(F)V":
                    print("{0}".format(stack.pop_float()))

                elif descriptor == "(Ljava/lang/String;)V":
                    j_str = stack.pop_ref()
                    py_str = StringPool.py_string(j_str)
                    print(py_str)

                else:
                    raise RuntimeError("println: " + method_ref.descriptor)

                # 方法返回时弹出当前栈帧
                stack.pop_ref()

                return

            raise RuntimeError("java.lang.NullPointerException")

        # 检测protected方法的调用权限
        if resolved_method.is_protected():
            if resolved_method.get_class().is_super_class_of(current_class) \
                    and resolved_method.get_class().get_package_name() != current_class.get_package_name() \
                    and obj_ref.get_class() != current_class \
                    and obj_ref.get_class().is_sub_class_of(current_class):
                raise RuntimeError("java.lang.IllegalAccessError")

        method_to_be_invoked = lookup_method_in_class(obj_ref.get_class(), method_ref.name, method_ref.descriptor)

        if method_to_be_invoked is None or method_to_be_invoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        invoke_method(frame, method_to_be_invoked)
