#!/usr/bin/env python
# encoding: utf-8
from email.policy import default


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
        d = ClassNameHelper.primitive_types.get(class_name)
        if d:
            return d

        return "L" +class_name + ";"

    @staticmethod
    def to_class_name(descriptor: str):
        if descriptor[0] == '[':
            return descriptor

        if descriptor[0] == 'L':
            return descriptor[1 : len(descriptor) - 1]

        # 原生
        for class_name, d in ClassNameHelper.primitive_types.items():
            if descriptor == d:
                return class_name

        raise RuntimeError("Invalid descriptor: " + descriptor)

    @staticmethod
    def get_component_class_name(class_name):
        if class_name[0] == '[':
            component_type_descriptor = class_name[1:]
            return ClassNameHelper.to_class_name(component_type_descriptor)

        raise RuntimeError("Not array: " + class_name)