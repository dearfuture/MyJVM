#!/usr/bin/env python
# encoding: utf-8
from rtda.Frame import Frame
from rtda.heap.Method import Method


def invoke_method(invoke_frame: Frame, method: Method):
    thread = invoke_frame.thread
    # 构造method的frame并设置为当前帧, 与return相对
    new_frame = thread.new_frame(method)
    thread.push_frame(new_frame)

    i = method.arg_slot_count -1
    while i >= 0:
        slot = invoke_frame.operand_stack.pop_slot()
        new_frame.local_vars.set_slot(i, slot)
        i -= 1
