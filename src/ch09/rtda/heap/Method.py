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
            # method = Method()
            # method.set_class(clazz)
            # method.copy_member_info(cf_method)
            # method.copy_attributes(cf_method)
            method = Method.new_method(clazz, cf_method)
            methods.append(method)

            # method.calc_arg_slot_count()
        return methods

    @staticmethod
    def new_method(clazz, cf_method: MemberInfo):
        method = Method()
        method.set_class(clazz)
        method.copy_member_info(cf_method)
        method.copy_attributes(cf_method)

        parsed_descriptor = MethodDescriptorParser.parse_method_descriptor(method.descriptor)
        method.calc_arg_slot_count(parsed_descriptor.parameter_types)

        # native method
        if method.is_native():
            method.inject_code_attribute(parsed_descriptor.return_type)

        return method


    # def calc_arg_slot_count(self):
    #     # 解析函数签名, 得到参数个数
    #     parsed_descriptor = MethodDescriptorParser.parse_method_descriptor(self.descriptor)
    #     for param_type in parsed_descriptor.parameter_types:
    #         self.arg_slot_count += 1
    #         # 本虚拟机没有对Long和Double做特殊处理
    #         # if param_type == "J" or "D":  self.arg_slot_count += 1
    #
    #     # 非静态方法要传递this
    #     if not self.is_static():
    #         self.arg_slot_count += 1

    def calc_arg_slot_count(self, parameter_types):
        for param_type in parameter_types:
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

    def inject_code_attribute(self, return_type):
        # 由于本地方法在class文件中没有Code属性, 所以需要给max_stack和max_locals赋值
        self.max_stack = 4
        self.max_locals = self.arg_slot_count

        # code字段是本地方法的字节码，第一条指令都是0xfe(INVOKE_NATIVE), 第二条指令则根据函数的返回值类型选择相应的返回指令
        if return_type[0] == 'V':
            # return
            self.code = [0xfe, 0xb1]
        elif return_type[0] == 'D':
            # dreturn
            self.code = [0xfe, 0xaf]
        elif return_type[0] == 'F':
            # freturn
            self.code = [0xfe, 0xae]
        elif return_type[0] == 'J':
            # lreturn
            self.code = [0xfe, 0xad]
        elif return_type[0] == 'L':
            # areturn
            self.code = [0xfe, 0xb0]
        else:
            # ireturn
            self.code = [0xfe, 0xac]