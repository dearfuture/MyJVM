#!/usr/bin/env python
# encoding: utf-8
from classfile.MemberInfo import MemberInfo
from rtda.heap import AccessFlags

class ClassMember:
    def __init__(self):
        # 访问标志
        self.access_flags = 0
        # 名字
        self.name = ""
        # 描述符
        self.descriptor = ""
        # 存放Class类指针
        self._class = None

    def copy_member_info(self, member_info: MemberInfo):
        self.access_flags = member_info.access_flags
        self.name = member_info.name
        self.descriptor = member_info.descriptor

    def set_class(self, clazz):
        self._class = clazz

    def get_class(self):
        return self._class

    # 用于判断public访问标志是否被设置
    def is_public(self):
        return 0 != self.access_flags & AccessFlags.ACC_PUBLIC

    # 用于判断private访问标志是否被设置
    def is_private(self):
        return 0 != self.access_flags & AccessFlags.ACC_PRIVATE

    # 用于判断protected访问标志是否被设置
    def is_protected(self):
        return 0 != self.access_flags & AccessFlags.ACC_PROTECTED

    # 用于判断static访问标志是否被设置
    def is_static(self):
        return 0 != self.access_flags & AccessFlags.ACC_STATIC

    # 用于判断final访问标志是否被设置
    def is_final(self):
        return 0 != self.access_flags & AccessFlags.ACC_FINAL

    # 用于判断synthetic访问标志是否被设置
    def is_synthetic(self):
        return 0 != self.access_flags & AccessFlags.ACC_SYNTHETIC

    def is_accessible_to(self, d):
        if self.is_public():
            return True
        c = self._class
        if self.is_protected():
            return d == c or c.get_package_name() == d.get_package_name() or d.is_sub_class_of(c)
        if not self.is_private():
            return c.get_package_name() == d.get_package_name()
        return d == c
