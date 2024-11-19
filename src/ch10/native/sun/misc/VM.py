#!/usr/bin/env python
# encoding: utf-8
from instructions.base import MethodInvokeLogic
from native import Registry
from rtda.Frame import Frame
from rtda.heap import StringPool

def initialize(frame: Frame):
    vm_class = frame.method.get_class()
    savedProps = vm_class.get_ref_var("savedProps", "Ljava/util/Properties;")
    key = StringPool.j_string(vm_class.loader, "foo")
    value = StringPool.j_string(vm_class.loader, "bar")

    frame.operand_stack.push_ref(savedProps)
    frame.operand_stack.push_ref(key)
    frame.operand_stack.push_ref(value)

    props_class = vm_class.loader.load_class("java/util/Properties")
    setProperty = props_class.get_instance_method("setProperty", "(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;")
    MethodInvokeLogic.invoke_method(frame, setProperty)

Registry.register("sun/misc/VM", "initialize", "()V", initialize)