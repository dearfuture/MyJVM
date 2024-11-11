#!/usr/bin/env python
# encoding: utf-8
from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame

def _numeric_return(frame: Frame):
    thread = frame.thread
    # 弹出当前帧, 与invoke_method对应
    current_frame = thread.pop_frame()
    # 获取调用帧
    invoke_frame = thread.top_frame
    ret_val = current_frame.operand_stack.pop_numeric()
    invoke_frame.operand_stack.push_numeric(ret_val)

class RETURN(NoOperandsInstruction):
    def execute(self, frame: Frame):
        frame.thread.pop_frame()

class ARETURN(NoOperandsInstruction):
    def execute(self, frame: Frame):
        thread = frame.thread
        current_frame = thread.current_frame
        invoke_frame = thread.top_frame
        ref = current_frame.operand_stack.pop_ref()
        invoke_frame.operand_stack.push_ref(ref)

class IRETURN(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _numeric_return(frame)

class LRETURN(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _numeric_return(frame)

class FRETURN(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _numeric_return(frame)

class DRETURN(NoOperandsInstruction):
    def execute(self, frame: Frame):
        _numeric_return(frame)



