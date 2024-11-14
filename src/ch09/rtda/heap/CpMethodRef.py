#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantMemberRefInfo import ConstantMethodRefInfo
from rtda.heap.CpMemberRef import MemberRef

from rtda.heap import MethodLookup


# MethodRef不包含接口方法，接口方法在InterfaceMethodRef类实现
class MethodRef(MemberRef):
    def __init__(self):
        super(MethodRef, self).__init__()
        self.method = None

    @staticmethod
    def new_method_ref(rt_constant_pool, ref_info: ConstantMethodRefInfo):
        ref = MethodRef()
        ref.rt_constant_pool = rt_constant_pool
        ref.copy_member_ref_info(ref_info)
        return ref

    def resolved_method(self):
        if self.method is None:
            self.resolved_method_ref()
        return self.method

    def resolved_method_ref(self):
        d = self.rt_constant_pool.clazz
        c = self.resolved_class()
        if c.is_interface():
            raise RuntimeError("java.lang.NoSuchMethodError")

        method = MethodLookup.lookup_method(c, self.name, self.descriptor)
        if method is None:
            raise RuntimeError("java.lang.NoSuchFieldError")
        if not method.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")
        self.method = method



