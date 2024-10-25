#!/usr/bin/env python
# encoding: utf-8
from classfile.ConstantInfo import ConstantInfo
from classfile.ClassReader import ClassReader

class ConstantPool:
    cp: [ConstantInfo]

    def __init__(self):
        self.cp = []

    # 读取class文件初始化constant_pool
    def read_constant_pool(self, class_reader: ClassReader):
        constant_pool_count = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        # 初始化长度为constant_pool_count的0数组
        self.cp = [0 for i in range(constant_pool_count)]

        # 1 ~ constant_pool_count-1
        i = 1
        while i < constant_pool_count:
            self.cp[i] = ConstantInfo.read_constant_info(class_reader, self.cp)
            if(self.cp[i].tag == ConstantInfo.CONSTANT_Long or self.cp[i].tag == ConstantInfo.CONSTANT_Double):
                # Long Double占两个数组位
                i += 1
            i += 1

    # constant_pool初始化完成后，根据index读取Utf8String的内容
    def get_utf8_str(self, index):
        # ConstantUft8StringInfo
        utf8_info = self.get_constant_info(index)
        return utf8_info.str

    # constant_pool初始化完成后，根据index读取constant_pool[index]
    def get_constant_info(self, index):
        constant_info = self.cp[index]
        if constant_info:
            return constant_info
        raise RuntimeError("Invalid constant pool index!")


    # 以下都涉及多级符号引用(多级索引寻址)

    # onstant_pool初始化完成后，根据index从constant_pool获取class_name。注意与get_utf8_str区分（入参的索引级别不同）
    def get_class_name(self, index):
        # ConstantClassInfo
        class_info = self.get_constant_info(index)
        #二次寻址根据ConstantClassInfo.name_index取得class_name
        return self.get_utf8_str(class_info.name_index)

    # constant_pool初始化完成后，根据index读取ConstantNameAndTypeInfo
    def get_name_and_type(self, index):
        # ConstantNameAndTypeInfo
        nt_info =  self.get_constant_info(index)
        name = self.get_utf8_str(nt_info.name_index)
        _type = self.get_utf8_str(nt_info.descriptor_index)
        return name, _type

    # def get_string: 已经定义了ConstantStringInfo.__str__()自动转换为str
