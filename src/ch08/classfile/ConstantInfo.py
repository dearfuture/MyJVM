#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod

from classfile.ClassReader import ClassReader
# from classfile.ConstantPool import ConstantPool

# from classfile.CpNumeric import ConstantIntegerInfo, ConstantFloatInfo, ConstantLongInfo, ConstantDoubleInfo
# from classfile.ConstantUtf8Info import ConstantUtf8Info
#
# from classfile.ConstantStringInfo import ConstantStringInfo
# from classfile.ConstantClassInfo import ConstantClassInfo
# from classfile.ConstantNameAndTypeInfo import ConstantNameAndTypeInfo
#
# from classfile.ConstantMemberRefInfo import ConstantFieldRefInfo, ConstantMethodRefInfo, ConstantInterfaceMethodRefInfo

class ConstantInfo(metaclass=ABCMeta):
    # {
    #     tag
    #     info[] --> 字面量(Integer/Float/Long/Double/Utf8) 或 索引
    # }

    # u1 ConstantInfo类型，ConstantInfo的公共字段
    tag: int

    # tag 常量值定义
    CONSTANT_Class = 7
    CONSTANT_FieldRef = 9
    CONSTANT_MethodRef = 10
    CONSTANT_InterfaceMethodRef = 11
    CONSTANT_String = 8
    CONSTANT_Integer = 3
    CONSTANT_Float = 4
    CONSTANT_Long = 5
    CONSTANT_Double = 6
    CONSTANT_NameAndType = 12
    CONSTANT_Utf8 = 1
    CONSTANT_MethodHandler = 15
    CONSTANT_MethodType = 16
    CONSTANT_InvokeDynamic = 18

    @abstractmethod
    def read_info(self, class_reader: ClassReader):
        pass

    @staticmethod
    def read_constant_info(class_reader: ClassReader, constant_pool: []):
        tag = int.from_bytes(class_reader.read_uint8(), byteorder="big")

        # 根据tag创建不同的ConstantInfo子类对象，如ConstIntegerInfo ConstantStringInfo
        constant_info = ConstantInfo.new_constant_info(tag, constant_pool)

        constant_info.tag = tag

        # 多态调用read_info读取class文件填充对象，如ConstIntegerInfo.read_info(class_reader) ConstantStringInfo.read_info(class_reader)
        constant_info.read_info(class_reader)

        return constant_info

    @staticmethod
    def new_constant_info(tag: int, constant_pool):
        from .CpNumeric import ConstantDoubleInfo, ConstantLongInfo, ConstantFloatInfo, ConstantIntegerInfo
        from .ConstantUtf8Info import ConstantUtf8Info
        from .ConstantStringInfo import ConstantStringInfo
        from .ConstantMemberRefInfo import ConstantFieldRefInfo, ConstantInterfaceMethodRefInfo, \
            ConstantMethodRefInfo
        from .ConstantNameAndTypeInfo import ConstantNameAndTypeInfo
        from .ConstantClassInfo import ConstantClassInfo
        from .CpInvokeDynamic import ConstantInvokeDynamicInfo, ConstantMethodHandleInfo, \
            ConstantMethodTypeInfo

        # 字面量literal：数字/Utf8String
        # 数字，CpNumeric.py
        if tag == ConstantInfo.CONSTANT_Integer:
            return ConstantIntegerInfo()
        elif tag == ConstantInfo.CONSTANT_Float:
            return ConstantFloatInfo()
        elif tag == ConstantInfo.CONSTANT_Long:
            return ConstantLongInfo()
        elif tag == ConstantInfo.CONSTANT_Double:
            return ConstantDoubleInfo()

        # Utf8String，可能被其他常量项索引
        elif tag == ConstantInfo.CONSTANT_Utf8:
            return ConstantUtf8Info()

        # 符号引用symbolic reference
        # 二级索引
        # 取出index,再根据index去ConstantPool取Utf8String
        elif tag == ConstantInfo.CONSTANT_String:
            return ConstantStringInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_Class:
            return ConstantClassInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_NameAndType:
            return ConstantNameAndTypeInfo(constant_pool)

        # 多级索引
        # ConstantMemberRefInfo.py，根据index去ConstantPool取ConstantClassInfo和ConstantNameAndTypeInfo
        elif tag == ConstantInfo.CONSTANT_FieldRef:
            return ConstantFieldRefInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_MethodRef:
            return ConstantMethodRefInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_InterfaceMethodRef:
            return ConstantInterfaceMethodRefInfo(constant_pool)

        #  invokebydynamic指令相关JDK1.7开始支持 由于需要加载父类如 Java/lang/Object, 必须实现
        elif tag == ConstantInfo.CONSTANT_MethodHandler:
            return ConstantMethodHandleInfo()
        elif tag == ConstantInfo.CONSTANT_MethodType:
            return ConstantMethodTypeInfo()
        elif tag == ConstantInfo.CONSTANT_InvokeDynamic:
            return ConstantInvokeDynamicInfo()

        else:
            raise RuntimeError("java.lang.ClassFormatError: INVALID constant pool tag!")



