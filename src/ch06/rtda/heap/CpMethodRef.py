#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantMemberRefInfo import ConstantMethodRefInfo
from rtda.heap.CpMemberRef import MemberRef

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