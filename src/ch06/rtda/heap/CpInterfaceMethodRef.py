#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantMemberRefInfo import ConstantInterfaceMethodRefInfo
from rtda.heap.CpMemberRef import MemberRef

class InterfaceMethodRef(MemberRef):
    def __init__(self):
        super(InterfaceMethodRef, self).__init__()
        self.method = None

    @staticmethod
    def new_interface_method_ref(rt_constant_pool, ref_info: ConstantInterfaceMethodRefInfo):
        ref = InterfaceMethodRef()
        ref.rt_constant_pool = rt_constant_pool
        ref.copy_member_ref_info(ref_info)
        return ref