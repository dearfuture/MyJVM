#!/usr/bin/env python
# encoding: utf-8

import os
from optparse import OptionParser

from classfile.ClassFile import ClassFile
from classpath.ClassPath import ClassPath
from Cmd import Cmd
from rtda.Frame import Frame
from rtda.LocalVars import LocalVars


def main(input_args):
    # 设置传入参数
    print("JVM ch04")

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

# 加载class
def load_class(class_name, class_path):
    class_data, _, error = class_path.read_class(class_name)

    class_file = ClassFile()
    cf = class_file.parse(class_data)
    return cf

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


def test_local_vars(local_vars: LocalVars):
    local_vars.set_numeric(0, 100)
    local_vars.set_numeric(1, -100)
    local_vars.set_numeric(2, 2997924580)
    local_vars.set_numeric(3, -2997924580)
    local_vars.set_numeric(4, 3.1415926)
    local_vars.set_numeric(5, 2.71828182845)

    local_vars.set_ref(6, None)

    print(local_vars.get_numeric(0))
    print(local_vars.get_numeric(1))
    print(local_vars.get_numeric(2))
    print(local_vars.get_numeric(3))
    print(local_vars.get_numeric(4))
    print(local_vars.get_numeric(5))
    print(local_vars.get_ref(6))

def test_operand_stack(ops):
    ops.push_numeric(100)
    ops.push_numeric(-100)
    ops.push_numeric(2997924580)
    ops.push_numeric(-2997924580)
    ops.push_numeric(3.1415926)
    ops.push_numeric(2.71828182845)

    ops.push_ref(None)

    print(ops.pop_ref())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())
    print(ops.pop_numeric())

# 启动JVM函数
def start_JVM(cmd):
    frame = Frame(100, 100)
    test_local_vars(frame.local_vars)
    print("----------------")
    test_operand_stack(frame.operand_stack)


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")

    # 指定-Xjre选项和类名
    fake_args = ['--Xjre', Xjre_path, 'java.lang.String']
    main(fake_args)


