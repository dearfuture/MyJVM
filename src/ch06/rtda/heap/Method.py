#!/usr/bin/env python
# encoding: utf-8
from classfile.MemberInfo import MemberInfo
from rtda.heap.ClassMember import ClassMember


class Method(ClassMember):
    def __init__(self):
        super(Method, self).__init__()
        self.max_stack = 0
        self.max_locals = 0
        self.code = []

    def copy_attributes(self, cf_method: MemberInfo):
        code_attr = cf_method.code_attributes
        if code_attr:
            self.max_stack = code_attr.max_stack
            self.max_locals = code_attr.max_locals
            self.code = code_attr.code

    @staticmethod
    def new_methods(clazz, cf_methods: [MemberInfo]):
        methods = []
        for cf_method in cf_methods:
            method = Method()
            method.set_class(clazz)
            method.copy_member_info(cf_method)
            method.copy_attributes(cf_method)
            methods.append(method)
        return methods


