#!/usr/bin/env python
# encoding: utf-8
from classfile.MemberInfo import MemberInfo
from rtda.heap.ClassMember import ClassMember


class Field(ClassMember):
    def __init__(self):
        super(Field, self).__init__()
        self.const_value_index = 0
        self.slot_id = 0

    @staticmethod
    def new_fields(clazz, cf_fields: [MemberInfo]):
        fields = []
        for cf_field in cf_fields:
            field = Field()
            field.set_class(clazz)
            field.copy_member_info(cf_field)
            field.copy_attribute(cf_field)

            fields.append(field)
        return fields

    def copy_attribute(self, cf_field: MemberInfo):
        val_attr = cf_field.constant_value_attribute()
        if val_attr:
            self.const_value_index = val_attr.constant_value_index

    def is_long_or_double(self):
        return self.descriptor == "J" or self.descriptor == "D"