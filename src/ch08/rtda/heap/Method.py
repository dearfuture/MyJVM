#!/usr/bin/env python
# encoding: utf-8
from classfile.MemberInfo import MemberInfo
from rtda.heap import AccessFlags
from rtda.heap.MethodDescriptorParser import MethodDescriptorParser
from rtda.heap.ClassMember import ClassMember


class Method(ClassMember):
    def __init__(self):
        super(Method, self).__init__()
        self.max_stack = 0
        self.max_locals = 0
        self.code = []
        self.arg_slot_count = 0

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

            method.calc_arg_slot_count()
        return methods

    def calc_arg_slot_count(self):
        # 解析函数签名, 得到参数个数
        parsed_descriptor = MethodDescriptorParser.parse_method_descriptor(self.descriptor)
        for param_type in parsed_descriptor.parameter_types:
            self.arg_slot_count += 1
            # 本虚拟机没有对Long和Double做特殊处理
            # if param_type == "J" or "D":  self.arg_slot_count += 1

        # 非静态方法要传递this
        if not self.is_static():
            self.arg_slot_count += 1

    def is_abstract(self):
        return 0 != self.access_flags & AccessFlags.ACC_ABSTRACT

    def is_native(self):
        return 0 != self.access_flags & AccessFlags.ACC_NATIVE
