#!/usr/bin/env python
# encoding: utf-8

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame
from rtda.heap import Object
from rtda.heap.StringPool import py_string


class ATHROW(NoOperandsInstruction):
    def execute(self, frame: Frame):
        exception = frame.operand_stack.pop_ref()
        if exception is None:
            raise RuntimeError("java.lang.NullPointerException")

        thread= frame.thread
        if not find_and_goto_exception_handler(thread, exception):
            handle_uncaught_exception(thread, exception)


def find_and_goto_exception_handler(thread, exception: Object):
    while True:
        frame = thread.current_frame
        pc = frame.next_pc - 1

        handler_pc = frame.method.find_exception_handler(exception.get_class(), pc)
        if handler_pc > 0:
            stack = frame.operand_stack
            stack.clear()
            stack.push_ref(exception)
            frame.next_pc = handler_pc
            return True

        thread.pop_frame()
        if thread.is_stack_empty():
            break

    return False

def handle_uncaught_exception(thread, exception: Object):
    thread.clear_stack()

    j_msg = exception.get_ref_var("detailMessage", "Ljava/lang/String;")
    py_msg = py_string(j_msg)
    print(exception.get_class().java_name() + ": " + py_msg)

    stes = exception.extra
    for ste in stes:
        print("\tat ", ste)
