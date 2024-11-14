#!/usr/bin/env python
# encoding: utf-8
from native import Registry
from rtda.Frame import Frame

# public final native Class<?> getClass();
def getClass(frame: Frame):
    this = frame.local_vars.get_ref(0)
    clazz = this.get_class().j_class
    frame.operand_stack.push_ref(clazz)

Registry.register("java/lang/Object", "getClass", "()Ljava/lang/Class;", getClass)