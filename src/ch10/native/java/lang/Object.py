#!/usr/bin/env python
# encoding: utf-8
from native import Registry
from rtda.Frame import Frame

# public final native Class<?> getClass();
def getClass(frame: Frame):
    this = frame.local_vars.get_ref(0)
    clazz = this.get_class().j_class
    frame.operand_stack.push_ref(clazz)

def hashCode(frame: Frame):
    this = frame.local_vars.get_ref(0)
    hash_value = hash(this)
    frame.operand_stack.push_numeric(hash_value)

def clone(frame: Frame):
    this = frame.local_vars.get_ref(0)

    # check Cloneable
    clazz = this.get_class()
    cloneable = clazz.loader.load_class("java/lang/Cloneable")
    if not clazz.is_implements(cloneable):
        raise RuntimeError("java.lang.CloneNotSupportedException")

    frame.operand_stack.push_ref(this.clone())


Registry.register("java/lang/Object", "getClass", "()Ljava/lang/Class;", getClass)
Registry.register("java/lang/Object", "hashCode", "()I", hashCode)
Registry.register("java/lang/Object", "clone", "()Ljava/lang/Object;", clone)