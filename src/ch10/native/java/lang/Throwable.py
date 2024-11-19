#!/usr/bin/env python
# encoding: utf-8
from native import Registry
from rtda.Frame import Frame
from rtda.Thread import Thread
from rtda.heap.Class import Class
from rtda.heap.Object import Object

# ste
class StackTraceElement:
    # 用于记录Java虚拟机栈帧信息
    def __init__(self):
        # 类所在的文件名
        self.file_name = ""
        # 声明方法的类名
        self.class_name = ""
        # 方法名
        self.method_name = ""
        # 帧正在执行的代码行号
        self.line_number = 0

    # 打印虚拟机栈
    def __str__(self):
        return "{0}.{1}({2}:{3})".format(self.class_name, self.method_name, self.file_name, self.line_number)

def fillInStackTrace(frame: Frame):
    this = frame.local_vars.get_ref(0)
    frame.operand_stack.push_ref(this)

    stes = create_stack_trace_elements(this, frame.thread)
    this.extra = stes

def create_stack_trace_elements(obj: Object, thread: Thread):
    skip = distance_to_object(obj.get_class()) + 2
    frames = thread.stack.get_frames()[skip:]
    stes = []
    for frame in frames:
        stes.append(create_stack_trace_element(frame))
    return stes

def create_stack_trace_element(frame: Frame):
    method = frame.method
    clazz = method.get_class()

    ste = StackTraceElement()
    ste.file_name = clazz.source_file
    ste.class_name = clazz.java_name()
    ste.method_name = method.name
    ste.line_number = method.get_line_number(frame.next_pc - 1)

    return ste

def distance_to_object(clazz: Class):
    distance = 0
    c = clazz.super_class
    while c != None:
        distance += 1
        c = c.super_class
    return distance




Registry.register("java/lang/Throwable", "fillInStackTrace", "(I)Ljava/lang/Throwable;", fillInStackTrace)