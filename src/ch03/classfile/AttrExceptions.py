#!/usr/bin/env python
# encoding: utf-8
from classfile.AttributeInfo import AttributeInfo

class ExceptionsAttribute(AttributeInfo):
    def __init__(self):
        self.exception_index_table = []

    def read_info(self, class_reader):
        self.exception_index_table = class_reader.read_uint16s()