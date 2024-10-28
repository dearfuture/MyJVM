#!/usr/bin/env python
# encoding: utf-8

# from classfile.AttrLineNumberTable import LineNumberTableAttribute
# from classfile.AttrLocalVariableTable import LocalVariableTableAttribute
# from classfile.AttrExceptions import ExceptionsAttribute
# from classfile.AttrConstantValue import ConstantValueAttribute
# from classfile.AttrSourceFile import SourceFileAttribute
# from classfile.AttrUnparsed import UnparsedAttribute
# from classfile.AttrCode import CodeAttribute
# from classfile.AttrMarkers import DeprecatedAttribute, SyntheticAttribute

from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool

from abc import ABCMeta, abstractmethod

class AttributeInfo:
    # 公共属性
    # u2
    # attribute_name_index = 0
    # u4
    # attribute_length = 0

    # u1    read_info()读出
    # attr_info

    attr_name_index = 0
    attr_name = ""

    @abstractmethod
    def read_info(self, class_reader):
        pass

    @staticmethod
    def read_attributes(class_reader:ClassReader, constant_pool:ConstantPool):
        attr_count = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        attributes = []
        for i in range(attr_count):
            attr_info = AttributeInfo.read_attribute(class_reader, constant_pool)
            attributes.append(attr_info)
        return attributes


    @staticmethod
    def read_attribute(class_reader:ClassReader, constant_pool:ConstantPool):
        attr_name_index = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        attr_name = ""
        # 注意会出现attr_name_index == 0的情况，必须加判断
        if attr_name_index != 0:
            attr_name = constant_pool.get_utf8_str(attr_name_index)
        # 注意这个length是u4，要用uint32读
        attr_length = int.from_bytes(class_reader.read_uint32(), byteorder="big")
        attr_info = AttributeInfo.new_attribute_info(attr_name, attr_length, constant_pool)
        attr_info.read_info(class_reader)
        attr_info.attr_name_index = attr_name_index
        attr_info.attr_name = attr_name
        return attr_info

    @staticmethod
    def new_attribute_info(attr_name, attr_len, constant_pool):
        from .AttrCode import CodeAttribute
        from .AttrConstantValue import ConstantValueAttribute
        from .AttrMarkers import DeprecatedAttribute, SyntheticAttribute
        from .AttrExceptions import ExceptionsAttribute
        from .AttrLineNumberTable import LineNumberTableAttribute
        from .AttrSourceFile import SourceFileAttribute
        from .AttrUnparsed import UnparsedAttribute
        from .AttrLocalVariableTable import LocalVariableTableAttribute

        if attr_name == "Deprecated":
            return DeprecatedAttribute()
        elif attr_name == "Synthetic":
            return SyntheticAttribute()

        # 核心
        elif attr_name == "Code":
            return CodeAttribute(constant_pool)
        elif attr_name == "ConstantValue":
            return ConstantValueAttribute(constant_pool)
        elif attr_name == "Exceptions":
            return ExceptionsAttribute()

        # 调试信息
        elif attr_name == "SourceFile":
            return SourceFileAttribute(constant_pool)
        elif attr_name == "LineNumberTable":
            return LineNumberTableAttribute()
        elif attr_name == "LocalVariableTable":
            return LocalVariableTableAttribute()



        else:
            return UnparsedAttribute(attr_name, attr_len)
