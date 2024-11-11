#!/usr/bin/env python
# encoding: utf-8
from rtda.heap.Class import Class


def lookup_method(clazz: Class, name: str, descriptor: str):
    method = lookup_method_in_class(clazz, name, descriptor)
    if method is None:
        # 已经在本类找过了
        method = lookup_method_in_class(clazz, name, descriptor, False)
    return method


def lookup_interface_method(clazz: Class, name: str, descriptor: str):
    return lookup_method_in_class(clazz, name, descriptor)



def lookup_method_in_class(clazz: Class, name: str, descriptor: str):
    c = clazz
    while c is not None:
        for method in c.methods:
            if method.name == name and method.descriptor == descriptor:
                return method

        c = c.super_class
    return None


def lookup_method_in_interfaces(clazz: Class, name: str, descriptor: str, search_self = True):
    if search_self:
        for method in clazz.methods:
            if method.name == name and method.descriptor == descriptor:
                return method

    for interface in clazz.interfaces:
        # 递归查找, interfaces为空时结束
        method = lookup_method_in_class(interface, name, descriptor)
        if method is None:
            return method
    return None

