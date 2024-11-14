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
    return char_array.chars.decode("utf-8")
