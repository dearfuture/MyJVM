#!/usr/bin/env python
# encoding: utf-8

registry = dict()

def register(class_name:str, method_name:str, method_descriptor:str, method):
    key = class_name + "-"  + method_name + "-" + method_descriptor
    registry[key] = method

def find_native_method(class_name:str, method_name:str, method_descriptor:str):
    key = class_name + "-" + method_name + "-" + method_descriptor
    method = registry.get(key)
    if method:
        return method

    if method_descriptor == "()V" and method_name == "registerNatives":
        return empty_native_method

    return None

def empty_native_method(frame):
    pass