#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantClassInfo import ConstantClassInfo
from rtda.heap.CpSymRef import SymRef

class ClassRef(SymRef):
    @staticmethod
    def new_class_ref(rt_constant_pool, class_info: ConstantClassInfo):
        ref = ClassRef()
        ref.rt_constant_pool = rt_constant_pool
        ref.class_name = class_info.name
        return ref

    # def resolved_class 在ClassRef实现
