#!/usr/bin/env python
# encoding: utf-8

from classfile.MemberInfo import MemberInfo
from instructions.InstructionFactory import InstructionFactory
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame
from rtda.Thread import Thread
from rtda.heap.Method import Method
from rtda.heap import StringPool

# 导入Class, Object执行Registry.register
from native.java.lang import Class
from native.java.lang import Object

class Interpreter:
    def __init__(self):
        pass

    # @staticmethod
    # def interpret(method_info: MemberInfo):
    #     code_attr = method_info.code_attributes
    #     max_locals = code_attr.max_locals
    #     max_stack = code_attr.max_stack
    #     bytecode = code_attr.code

    @staticmethod
    def create_args_array(class_loader, args):
        string_class = class_loader.load_class("java/lang/String")
        args_array = string_class.array_class().new_array(len(args))
        j_args = args_array.refs
        for i, arg in enumerate(args):
            j_args[i] = StringPool.j_string(class_loader, arg)
        return args_array

    @staticmethod
    # def interpret(method: Method):
    def interpret(method: Method, args):
        thread = Thread()
        frame = thread.new_frame(method)
        thread.push_frame(frame)

        if len(args) > 0:
            j_args = Interpreter.create_args_array(method.get_class().loader, args)
            frame.local_vars.set_ref(0, j_args)

        try:
            # Interpreter.loop(thread, True)
            Interpreter.loop(thread, False)
        except RuntimeError as e:
            Interpreter.log_frames(thread)
            print("LocalVars: {0}".format(frame.local_vars))
            print("OperandStack: {0}".format(frame.operand_stack))
            print(e)

    @staticmethod
    def loop(thread: Thread, log_inst: bool):
        bytecode_reader = BytecodeReader()
        inst_count = 0

        while True:
            frame = thread.current_frame
            pc = frame.next_pc
            thread.pc = pc

            bytecode_reader.reset(frame.method.code, pc)
            opcode = bytecode_reader.read_uint8()
            instruction = InstructionFactory.new_instruction(opcode)
            instruction.fetch_operands(bytecode_reader)
            frame.next_pc = bytecode_reader.pc

            inst_count += 1
            # print("inst_count={0}".format(inst_count))

            if log_inst:
                Interpreter.log_instruction(frame, instruction, opcode)

            instruction.execute(frame)

            if thread.is_stack_empty():
                break

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

    @staticmethod
    def log_instruction(frame, instruction, opcode):
        method = frame.method
        class_name = method.get_class().name
        method_name = method.name
        pc = frame.thread.pc

        print("{0}.{1}() #{2:<2} {3} {4} {5} operand_stack: {6} local_vars: {7}".format(class_name, method_name, pc,
                                                                                        hex(opcode),
                                                                                        instruction.__class__.__name__,
                                                                                        Interpreter.print_obj(
                                                                                            instruction),
                                                                                        frame.operand_stack,
                                                                                        frame.local_vars))