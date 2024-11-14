#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantInfo import ConstantInfo
from classfile.ConstantPool import ConstantPool
from rtda.heap.CpClassRef import ClassRef
from rtda.heap.CpFieldRef import FieldRef
from rtda.heap.CpInterfaceMethodRef import InterfaceMethodRef
from rtda.heap.CpMethodRef import MethodRef


class RuntimeConstantPool:
    consts: []
    def __init__(self, clazz, consts: []):
        self.clazz = clazz
        self.consts = consts

    @staticmethod
    def new_rt_constant_pool(clazz, constant_pool: ConstantPool):
        cp_count = len(constant_pool.cp)
        consts = [None for i in range(cp_count)]
        rt_constant_pool = RuntimeConstantPool(clazz, consts)

        # 把classfile.ConstantPool.cp 的内容(转换成值) 复制到 heap.RuntimeConstantPool.consts
        i = 1
        while i < cp_count:
            cp_info = constant_pool.cp[i]
            if cp_info:
                if cp_info.tag == ConstantInfo.CONSTANT_Long or cp_info.tag == ConstantInfo.CONSTANT_Double:
                    consts[i] = cp_info.val
                    i += 1
                elif cp_info.tag == ConstantInfo.CONSTANT_Integer or cp_info.tag == ConstantInfo.CONSTANT_Float:
                    consts[i] = cp_info.val

            # 不会出现Utf8
            # elif cp_info.tag == ConstantInfo.CONSTANT_Utf8:
            #     consts[i] = cp_info.str
            # elif cp_info.tag == ConstantInfo.CONSTANT_NameAndType:

                elif cp_info.tag == ConstantInfo.CONSTANT_String:
                    consts[i] = str(cp_info)
                elif cp_info.tag == ConstantInfo.CONSTANT_Class:
                    consts[i] = ClassRef.new_class_ref(rt_constant_pool, cp_info)

                # 多级索引
                # ConstantMemberRefInfo.py，根据index去ConstantPool取ConstantClassInfo和ConstantNameAndTypeInfo
                elif cp_info.tag == ConstantInfo.CONSTANT_FieldRef:
                    consts[i] = FieldRef.new_field_ref(rt_constant_pool, cp_info)
                elif cp_info.tag == ConstantInfo.CONSTANT_MethodRef:
                    consts[i] = MethodRef.new_method_ref(rt_constant_pool, cp_info)
                elif cp_info.tag == ConstantInfo.CONSTANT_InterfaceMethodRef:
                    consts[i] = InterfaceMethodRef.new_interface_method_ref(rt_constant_pool, cp_info)

            i += 1

        return rt_constant_pool

    def get_class(self):
        return self.clazz

    # 根据索引返回常量
    def get_constant(self, index):
        c = self.consts[index]
        if c is not None:
            return c
        else:
            raise RuntimeError("No constants at index {0}".format(index))