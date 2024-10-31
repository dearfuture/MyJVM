#!/usr/bin/env python
# encoding: utf-8
from classfile.MemberInfo import MemberInfo
from instructions.InstructionFactory import InstructionFactory
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame
from rtda.Thread import Thread



class Interpreter:
    def __init__(self):
        pass

    @staticmethod
    def interpret(method_info: MemberInfo):
        code_attr = method_info.code_attributes
        max_locals = code_attr.max_locals
        max_stack = code_attr.max_stack
        bytecode = code_attr.code

        thread = Thread()
        frame = thread.new_frame(max_locals, max_stack)
        thread.push_frame(frame)

        # Interpreter.loop(thread, bytecode)
        try:
            Interpreter.loop(thread, bytecode)
        except RuntimeError as e:
            Interpreter.log_frames(thread)
            print("LocalVars: {0}".format(frame.local_vars))
            print("OperandStack: {0}".format(frame.operand_stack))
            print(e)

    @staticmethod
    def loop(thread: Thread, bytecode: bytes):
        frame = thread.pop_frame()
        bytecode_reader = BytecodeReader()

        while True:
            pc = frame.next_pc
            thread.pc = pc

            bytecode_reader.reset(bytecode, pc)
            opcode = bytecode_reader.read_uint8()
            instruction = InstructionFactory.new_instruction(opcode)
            instruction.fetch_operands(bytecode_reader)
            frame.next_pc = bytecode_reader.pc

            print("pc:{0} opcode:{1} inst:{2} [{3}]".format(pc, hex(opcode), instruction.__class__.__name__, Interpreter.print_obj(instruction)))
            instruction.execute(frame)

    @staticmethod
    def print_obj(obj):
        return ' '.join(['%s:%s' % item for item in obj.__dict__.items()])

    @staticmethod
    def log_frames(thread):
        while not thread.is_stack_empty():
            frame = thread.pop_frame()
            method = frame.method
            class_name = method.get_class().name
            print(">> pc: {0:4} {1}.{2}{3}".format(frame.next_pc, class_name, method.name, method.descriptor))