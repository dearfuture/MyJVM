#!/usr/bin/env python
# encoding: utf-8

from classfile.ConstantMemberRefInfo import ConstantMemberRefInfo
from rtda.heap.CpSymRef import SymRef


class MemberRef(SymRef):
    def __init__(self):
        super(MemberRef, self).__init__()
        self.class_name = ""
        self.name = ""
        self.descriptor = ""

    def copy_member_ref_info(self, ref_info: ConstantMemberRefInfo):
        self.class_name = ref_info.class_name
        self.name, self.descriptor = ref_info.name_and_type
