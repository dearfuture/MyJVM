#!/usr/bin/env python
# encoding: utf-8

class ExceptionTable:
    def __init__(self):
        self.exception_table = []

    def find_exception_handler(self, clazz, pc):
        for handler in self.exception_table:
            if pc >= handler.start_pc and pc < handler.end_pc:
                # catch-all
                if handler.catch_type is None:
                    return handler
                catch_class = handler.catch_type.resolved_class()
                if catch_class == clazz or catch_class.is_super_class_of(clazz):
                    return handler
        return None


    @staticmethod
    def new_exception_table(entries, rt_constant_pool):
        et = ExceptionTable()
        for entry in entries:
            exception_handler = ExceptionHandler()
            exception_handler.start_pc = entry.start_pc
            exception_handler.end_pc = entry.end_pc
            exception_handler.handler_pc = entry.handler_pc
            if entry.catch_type == 0:
                # catch-all
                exception_handler.catch_type = None
            else:
                exception_handler.catch_type = rt_constant_pool.get_constant(entry.catch_type)

            et.exception_table.append(exception_handler)

        return et


class ExceptionHandler:
    def __init__(self):
        self.start_pc = 0
        self.end_pc = 0
        # 指出负责异常处理的catch{}块的位置
        self.handler_pc = 0
        # catch_type是个索引，通过它可以从运行时常量池中查到一个类符号引用。
        self.catch_type = None
