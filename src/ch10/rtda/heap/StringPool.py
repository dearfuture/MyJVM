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
    # chars = py_str.encode('utf-8')
    chars = string_to_utf16(py_str)
    j_chars = Object(class_loader.load_class("[C"), chars)

    j_str = class_loader.load_class("java/lang/String").new_object()
    j_str.set_ref_var("value", "[C", j_chars)

    interned_strings[py_str] = j_str

    return j_str

def py_string(j_str):
    char_array = j_str.get_ref_var("value", "[C")
    # if not isinstance(char_array, bytes):
    #     char_array.data = bytes(char_array.data)
    # 把字符数组转换成python字符串
    # return char_array.chars.decode('utf-8')
    return utf16_to_string(char_array.chars)

# 把python字符串（utf-8格式）转成Java字符数组（utf-16格式）
def string_to_utf16(s):
    """
    不能采用直接utf-8编码[s.encode("utf-8")]的原因：由于在python中存储的是字符串汉字（一个字符串表示三个字符，即三个整数），
    但是在Java中只能是一个汉字字符表示一个整数
    :param s:
    :return:
    """
    return [ord(char) for char in s]

def utf16_to_string(data):
    return "".join([chr(d) for d in data])

def intern_string(j_str):
    py_str = py_string(j_str)
    interned_str = interned_strings.get(py_str)
    if interned_str:
        return interned_str
    interned_strings[py_str] = j_str
    return j_str
