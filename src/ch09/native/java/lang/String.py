#!/usr/bin/env python
# encoding: utf-8
from native import Registry
from rtda.Frame import Frame
from rtda.heap import StringPool

def intern(frame: Frame):
    this = frame.local_vars.get_ref(0)
    interned = StringPool.intern_string(this)
    frame.operand_stack.push_ref(interned)

Registry.register("java/lang/String", "intern", "()Ljava/lang/String;", intern)