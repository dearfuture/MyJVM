#!/usr/bin/env python
# encoding: utf-8
from native import Registry
from rtda.Frame import Frame
from rtda.heap import StringPool


# def init():
#     Registry.register("java/lang/Class", "getPrimitiveClass", "(Ljava/lang/String;)Ljava/lang/Class;", getPrimitiveClass)
#     Registry.register("java/lang/Class", "getName0", "()Ljava/lang/String;", getName0)
#     Registry.register("java/lang/Class", "desireAssertionStatus0", "(Ljava/lang/Class;)Z", desireAssertionStatus0)

# static native Class<?> getPrimitiveClass(String name);
def getPrimitiveClass(frame: Frame):
    # j_string
    new_obj = frame.local_vars.get_ref(0)
    # py_string
    name = StringPool.py_string(new_obj)

    class_loader = frame.method.get_class().loader
    class_obj = class_loader.load_class(name).j_class

    frame.operand_stack.push_ref(class_obj)

# native String getName0();
def getName0(frame: Frame):
    # 实例方法的this对象
    this = frame.local_vars.get_ref(0)
    clazz = this.extra

    name = clazz.java_name()
    name_obj = StringPool.j_string(clazz.loader, name)

    frame.operand_stack.push_ref(name_obj)

def desiredAssertionStatus0(frame: Frame):
    frame.operand_stack.push_numeric(0)

Registry.register("java/lang/Class", "getPrimitiveClass", "(Ljava/lang/String;)Ljava/lang/Class;", getPrimitiveClass)
Registry.register("java/lang/Class", "getName0", "()Ljava/lang/String;", getName0)
Registry.register("java/lang/Class", "desiredAssertionStatus0", "(Ljava/lang/Class;)Z", desiredAssertionStatus0)
