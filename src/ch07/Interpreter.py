#!/usr/bin/env python
# encoding: utf-8

from classfile.MemberInfo import MemberInfo
from instructions.InstructionFactory import InstructionFactory
from instructions.base.BytecodeReader import BytecodeReader
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame
from rtda.Thread import Thread
from rtda.heap.Method import Method

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
    def interpret(method: Method):
        thread = Thread()
        frame = thread.new_frame(method)
        thread.push_frame(frame)
        # bytecode = method.code

        try:
            Interpreter.loop(thread, True)
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

            # if frame.method.name.find("<clinit>") == -1:
            inst_count += 1
            print("inst_count={0}".format(inst_count))

            if log_inst:
                Interpreter.log_instruction(frame, instruction, opcode)

            # print("pc:{0} opcode:{1} inst:{2} [{3}]".format(pc, hex(opcode), instruction.__class__.__name__, Interpreter.print_obj(instruction)))
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

        print("{0}.{1}() #{2:<2} {3} {4} operand_stack: {5} local_vars: {6}".format(class_name, method_name, pc,
                                                                                    instruction.__class__.__name__,
                                                                                    Interpreter.print_obj(instruction),
                                                                                    frame.operand_stack,
                                                                                    frame.local_vars))