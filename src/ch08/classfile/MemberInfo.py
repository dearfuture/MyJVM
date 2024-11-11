#!/usr/bin/env python
# encoding: utf-8
from classfile.AttrCode import CodeAttribute
from classfile.ClassReader import ClassReader
from classfile.AttributeInfo import AttributeInfo
from classfile.ConstantPool import ConstantPool

# filed method共用的结构体
class MemberInfo:
    constant_pool: ConstantPool
    # u2
    access_flags: int
    # u2
    name_index: int
    # u2
    descriptor_index: int
    attributes: [AttributeInfo]

    def __init__(self, constant_pool, access_flags, name_index, descriptor_index, attributes):
        self.constant_pool = constant_pool
        self.access_flags = access_flags
        self.name_index = name_index
        self.descriptor_index = descriptor_index
        self.attributes = attributes

    # 第一次调用获取fields{field_count, field_infos[]}，第二次调用获取methods{method_count, method_infos[]}
    @staticmethod
    def read_members(class_reader:ClassReader, constant_pool:ConstantPool):
        member_infos = []
        member_count = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        for i in range(member_count):
            member_infos.append(MemberInfo.read_member(class_reader, constant_pool))
        return member_infos

    @staticmethod
    def read_member(class_reader:ClassReader, constant_pool:ConstantPool):
        access_flags = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        name_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        descriptor_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        attributes = AttributeInfo.read_attributes(class_reader, constant_pool)
        return MemberInfo(constant_pool, access_flags, name_index, descriptor_index, attributes)

    @property
    def name(self):
        return self.constant_pool.get_utf8_str(self.name_index)

    @property
    def descriptor(self):
        return self.constant_pool.get_utf8_str(self.descriptor_index)

    @property
    def code_attributes(self) -> CodeAttribute:
        for attribute in self.attributes:
            if attribute.attr_name == "Code":
                return attribute
        return None


    def constant_value_attribute(self):
        for attribute in self.attributes:
            if attribute.attr_name == "ConstantValue":
                return attribute
        return None