#!/usr/bin/env python
# encoding: utf-8

from rtda.heap.Object import Object

# 字符串池
interned_strings = dict()


def j_string(class_loader, py_str):
    interned_str = interned_strings.get(py_str)
    if interned_str:
        return interned_str

    # utf-16
    chars = py_str.encode('utf-8')
    j_chars = Object(class_loader.load_class("[C"), chars)

    j_str = class_loader.load_class("java/lang/String").new_object()
    j_str.set_ref_var("value", "[C", j_chars)

    interned_strings[py_str] = j_str

    return j_str


def py_string(j_str):
    char_array = j_str.get_ref_var("value", "[C")
    if not isinstance(char_array, bytes):
        char_array.data = bytes(char_array.data)
    # 把字符数组转换成python字符串
    return char_array.chars.decode('utf-8')

def intern_string(j_str):
    py_str = py_string(j_str)
    interned_str = interned_strings.get(py_str)
    if interned_str:
        return interned_str
    interned_strings[py_str] = j_str
    return j_str
