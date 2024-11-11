from classfile.ClassReader import ClassReader
from classfile.AttributeInfo import AttributeInfo
from classfile.ConstantPool import ConstantPool


class CodeAttribute(AttributeInfo):
    constant_pool: ConstantPool
    # u2
    max_stack = 0
    # u2
    max_locals = 0
    # u4
    code_length = 0
    # u1
    code = []
    #u2
    # exception_table_length = 0
    # ExceptionTableEntry表
    exception_table = []
    # u2
    # attribute_count = 0
    # AttributeInfo表
    attributes = []


    def __init__(self, constant_pool: ConstantPool):
        self.constant_pool = constant_pool

    def read_info(self, class_reader: ClassReader):
        self.max_stack = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        self.max_locals = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        self.code_length = int.from_bytes(class_reader.read_uint32(), byteorder="big")
        self.code = class_reader.read_bytes(self.code_length)
        self.exception_table = ExceptionTableEntry.read_exception_table(class_reader)
        self.attributes = AttributeInfo.read_attributes(class_reader, self.constant_pool)

class ExceptionTableEntry():
    # u2
    start_pc = 0
    # u2
    end_pc = 0
    # u2
    handler_pc = 0
    # u2
    catch_type = 0

    def __init__(self, start_pc, end_pc, handler_pc, catch_type):
        self.start_pc = start_pc
        self.end_pc = end_pc
        self.handler_pc = handler_pc
        self.catch_type = catch_type

    @staticmethod
    def read_exception_table(class_reader: ClassReader):
        exception_table_length = int.from_bytes(class_reader.read_uint16(), byteorder="big")
        exception_table = []
        for i in range(exception_table_length):
            start_pc = int.from_bytes(class_reader.read_uint16(), byteorder="big")
            end_pc = int.from_bytes(class_reader.read_uint16(), byteorder="big")
            handler_pc = int.from_bytes(class_reader.read_uint16(), byteorder="big")
            catch_type = int.from_bytes(class_reader.read_uint16(), byteorder="big")
            exception_table_entry = ExceptionTableEntry(start_pc, end_pc, handler_pc, catch_type)
            exception_table.append(exception_table_entry)
        return exception_table