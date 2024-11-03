#!/usr/bin/env python
# encoding: utf-8

import os
from optparse import OptionParser

from Interpreter import Interpreter
from classfile.ClassFile import ClassFile
from classpath.ClassPath import ClassPath
from Cmd import Cmd
from rtda.Frame import Frame
from rtda.LocalVars import LocalVars
from rtda.OperandStack import OperandStack
from rtda.heap.Class import Class
from rtda.heap.ClassLoader import ClassLoader
from rtda.heap.Method import Method



def main(input_args):
    # 设置传入参数
    print("JVM ch06")

    parser = OptionParser(usage="usage:%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="version_flag",
                      help="print version and exit.")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--Xjre", action="store", type="string", dest="XjreOption", help="path to jre")
    # 解析参数
    (options, args) = parser.parse_args(input_args)
    if options:
        cmd = Cmd(options, args)

        if not options.version_flag:
            # 启动JVM
            start_JVM(cmd)

# 把class文件的一些重要信息打印出来
def print_class_info(class_file):
    print("version: {0}.{1}".format(class_file.major_version, class_file.minor_version))
    print("constants count: {0}".format(len(class_file.constant_pool.cp)))
    print("access flags: {0}".format(hex(int.from_bytes(class_file.access_flags, byteorder="big"))))
    print("this class: {0}".format(class_file.class_name))
    print("super class: {0}".format(class_file.super_class_name))
    print("interfaces: {0}".format(class_file.interface_names))
    print("fields count: {0}".format(len(class_file.fields)))
    for f in class_file.fields:
        print("   {0}".format(f.name))
    print("methods count: {0}".format(len(class_file.methods)))
    for m in class_file.methods:
        print("   {0}".format(m.name))

# 加载class
def load_class(class_name, class_path):
    class_data, _, error = class_path.read_class(class_name)

    class_file = ClassFile()
    cf = class_file.parse(class_data)
    return cf

# 被Class的get_main_method取代
# def get_main_method(class_file: ClassFile):
#     for method in class_file.methods:
#         if method.name == "main" and method.descriptor == "([Ljava/lang/String;)V":
#             return method
#     return None

# 启动JVM函数
def start_JVM(cmd):
    # 解析类路径
    class_path = ClassPath.parse(cmd.XjreOption, cmd.cpOption)
    # 打印命令行参数
    print("classpath: {0} class: {1} args: {2}".format(class_path, cmd.class_name, cmd.args))

    # 读取主类数据
    class_name = cmd.class_name.replace(".", "/")

    # class_data, _, error = class_path.read_class(class_name)
    # if error:
    #     print("Could not find or load main class {0}\n".format(cmd.class_name))
    #     exit(0)
    # 打印class里面的数据信息
    # print("class data: {0}".format([int(hex(d), 16) for d in class_data]))

    # class_file = load_class(class_name, class_path)
    # clazz = Class.new_class(class_file)
    # main_method = clazz.get_main_method()

    # 改用类加载器加载
    class_loader = ClassLoader(class_path)
    main_class = class_loader.load_class(class_name)
    main_method = main_class.get_main_method()

    if main_method:
        bytecode = main_method.code
        hex_string = ' '.join(f'{byte:02x}' for byte in bytecode)
        print(hex_string)
        Interpreter.interpret(main_method)

    else:
        print("Main method not found")

if __name__ == '__main__':

    print("TEST OperandStack BEGIN")
    stack = OperandStack(8)

    from rtda.heap.Object import Object
    obj = Object(Class())
    stack.push_ref(obj)

    # 模拟错误的DUP
    slot = stack.pop_slot()
    stack.push_slot(slot)
    # 应该手动拷贝slot再push
    stack.push_slot(slot)

    print("Before pop_ref: stack.size={0} stack.slots[0].ref={1}, stack.slots[1].ref={2}".format(stack.size, stack.slots[0].ref, stack.slots[1].ref) )
    # 同时破坏了stack.Slots[1]和stack.Slots[0]
    stack.pop_ref()
    print("After pop_ref:  stack.size={0} stack.slots[0].ref={1}, stack.slots[1].ref={2}".format(stack.size, stack.slots[0].ref, stack.slots[1].ref) )
    # ref = stack.pop_ref()
    print("TEST OperandStack END")


    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")

    # 指定-Xjre选项和类名
    resources_path = "F:\\JVM\\MyJVM\\java\\class"

    fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch06.MyObject']

    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch06.FieldInitTest']
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch06.FieldResolutionTest']
    # invokestatic 0xb8
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch06.FieldTest']

    main(fake_args)


