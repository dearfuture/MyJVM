#!/usr/bin/env python
# encoding: utf-8
from rtda.Frame import Frame
from rtda.heap.Method import Method

def init_class(thread, clazz):
    clazz.init_started = True
    schedule_clinit(thread, clazz)
    init_super_class(thread, clazz)

def schedule_clinit(thread, clazz):
    clinit = clazz.get_clinit_method()
    if clinit:
        new_frame = thread.new_frame(clinit)
        thread.push_frame(new_frame)

def init_super_class(thread, clazz):
    if not clazz.is_interface():
        super_class = clazz.super_class
        if super_class != None and not super_class.init_started:
            # 间接递归
            init_class(thread, super_class)