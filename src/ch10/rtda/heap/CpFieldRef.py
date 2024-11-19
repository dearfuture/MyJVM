#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantMemberRefInfo import ConstantFieldRefInfo
from rtda.heap.CpMemberRef import MemberRef

class FieldRef(MemberRef):
    def __init__(self):
        super(FieldRef, self).__init__()
        self.field = None
        self.rt_constant_pool = None

    @staticmethod
    def new_field_ref(rt_constant_pool, ref_info: ConstantFieldRefInfo):
        ref = FieldRef()
        ref.rt_constant_pool = rt_constant_pool
        ref.copy_member_ref_info(ref_info)
        return ref

    def resolved_field(self):
        if self.field is None:
            self.resolve_field_ref()
        return self.field

    def resolve_field_ref(self):
        d = self.rt_constant_pool.clazz
        c = self.resolved_class()
        field = FieldRef.lookup_field(c, self.name, self.descriptor)

        if field is None:
            raise RuntimeError("java.lang.NoSuchFieldError")
        if not field.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.field = field

    @staticmethod
    def lookup_field(clazz, name: str, descriptor: str):
        # 查找本类的属性，递归出口
        for field in clazz.fields:
            if field.name == name and field.descriptor == descriptor:
                return field

        for interface in clazz.interfaces:
            field = FieldRef.lookup_field(interface, name, descriptor)
            if field :
                return field

        # 递归从父类查找
        if clazz.super_class:
            return FieldRef.lookup_field(clazz.super_class, name, descriptor)

        return None

