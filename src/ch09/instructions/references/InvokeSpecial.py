#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import Index16Instruction
from instructions.base.MethodInvokeLogic import invoke_method
from rtda.Frame import Frame
from rtda.heap.MethodLookup import lookup_method, lookup_method_in_class


class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame: Frame):
        current_method = frame.method
        current_class = current_method.get_class()
        rt_constant_pool = current_class.rt_constant_pool
        method_ref = rt_constant_pool.get_constant(self.index)

        # SymRef.resolved_class() -> MethodRef
        resolve_class = method_ref.resolved_class()
        resolved_method = method_ref.resolved_method()

        # 构造方法
        if resolved_method.name == "<init>" and resolved_method.get_class() != resolve_class:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if resolved_method.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        # INVOKE_SPECIAL就是obj_ref.method(xxx,yyy,zzz)的最后一步
        # 执行INVOKE_SPECIAL前的压栈顺序是obj_ref, xxx, yyy, zzz...
        # 所以准备执行INVOKE_SPECIAL时operand_stack.slots[size-1 - (arg_slot_count-1)]就是obj_ref
        obj_ref = frame.operand_stack.get_ref_from_top(resolved_method.arg_slot_count - 1)
        if obj_ref is None:
            raise RuntimeError("java.lang.NullPointerException")

        # 检测protected方法的调用权限
        if resolved_method.is_protected():
            if resolved_method.get_class().is_super_class_of(current_class) \
                and resolved_method.get_class().get_package_name() != current_class.get_package_name() \
                and obj_ref.get_class() != current_class \
                and obj_ref.get_class().is_sub_class_of(current_class):
                raise RuntimeError("java.lang.IllegalAccessError")

        # 调用了父类的方法
        method_to_be_invoked = resolved_method
        if current_class.is_super():
            if resolve_class.is_super_class_of(current_class) \
                and resolved_method.name != "<init>":
                method_to_be_invoked = lookup_method_in_class(current_class.super_class, method_ref.name, method_ref.descriptor)

        # 检查是否是抽象方法
        if method_to_be_invoked is None or method_to_be_invoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        # 通过权限检查后调用
        invoke_method(frame, method_to_be_invoked)
