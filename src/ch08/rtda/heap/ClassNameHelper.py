#!/usr/bin/env python
# encoding: utf-8

class ClassNameHelper:
    primitive_types = {"void": "V",
                       "int": "I",
                       "long": "L",
                       "float": "F",
                       "double": "D",
                       "boolean": "Z",
                       "byte": "B",
                       "short": "S",
                       "char": "C"}

    @staticmethod
    def get_array_class_name(class_name):
        return "[" + ClassNameHelper.to_descriptor(class_name)

    @staticmethod
    def to_descriptor(class_name):
        if class_name[0] == '[':
            return class_name

        # 原生
        d = ClassNameHelper.primitive_types[class_name]
        if d:
            return d

        return "L" +class_name + ";"


