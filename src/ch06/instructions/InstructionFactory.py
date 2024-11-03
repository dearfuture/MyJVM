#!/usr/bin/env python
# encoding: utf-8
from instructions.comparsions.Ifcond import IFEQ, IFNE, IFLT, IFGE, IFGT, IFLE
from instructions.comparsions.Ificmp import IF_ICMPLE
from instructions.constants.Const import ICONST_0, ICONST_1, ICONST_M1, ACONST_NULL
from instructions.constants.Ipush import BIPUSH
from instructions.constants.Ldc import LDC_W, LDC, LDC2_W
from instructions.constants.Nop import NOP
from instructions.control.Goto import GOTO
from instructions.loads.Aload import ALOAD, ALOAD_1, ALOAD_2, ALOAD_3
from instructions.loads.Iload import ILOAD_2, ILOAD_1
from instructions.math.Add import IADD
from instructions.math.Iinc import IINC
from instructions.references.CheckCast import CHECK_CAST
from instructions.references.GetField import GET_FIELD
from instructions.references.GetStatic import GET_STATIC
from instructions.references.InstanceOf import INSTANCE_OF
from instructions.references.InvokeSpecial import INVOKE_SPECIAL
from instructions.references.InvokeVirtual import INVOKE_VIRTUAL
from instructions.references.New import NEW
from instructions.references.PutField import PUT_FIELD
from instructions.references.PutStatic import PUT_STATIC
from instructions.stack.Dup import DUP
from instructions.stores.Astore import ASTORE, ASTORE_1, ASTORE_2, ASTORE_3
from instructions.stores.Istore import ISTORE_1, ISTORE_2


class InstructionFactory:
    @staticmethod
    def new_instruction(opcode):
        if opcode == 0x00:
            return NOP()
        elif opcode == 0x01:
            return ACONST_NULL()
        elif opcode == 0x02:
            return ICONST_M1()
        elif opcode == 0x03:
            return ICONST_0()
        elif opcode == 0x04:
            return ICONST_1()

        elif opcode == 0x10:
            return BIPUSH()
        elif opcode == 0x12:
            return LDC()
        elif opcode == 0x13:
            return LDC_W()
        elif opcode == 0x14:
            return LDC2_W()

        elif opcode == 0x19:
            return ALOAD()
        elif opcode == 0x1b:
            return ILOAD_1()
        elif opcode == 0x1c:
            return ILOAD_2()

        elif opcode == 0x2b:
            return ALOAD_1()
        elif opcode == 0x2c:
            return ALOAD_2()
        elif opcode == 0x2d:
            return ALOAD_3()

        elif opcode == 0x3a:
            return ASTORE()
        elif opcode == 0x3c:
            return ISTORE_1()

        elif opcode == 0x3c:
            return ISTORE_1()
        elif opcode == 0x3d:
            return ISTORE_2()

        elif opcode == 0x4c:
            return ASTORE_1()
        elif opcode == 0x4d:
            return ASTORE_2()
        elif opcode == 0x4e:
            return ASTORE_3()

        elif opcode == 0x59:
            return DUP()

        elif opcode == 0x60:
            return IADD()

        elif opcode == 0x84:
            return IINC()

        elif opcode == 0xa4:
            return IF_ICMPLE()
        elif opcode == 0xa7:
            return GOTO()

        elif opcode == 0x99:
            return IFEQ()
        elif opcode == 0x9a:
            return IFNE()
        elif opcode == 0x9b:
            return IFLT()
        elif opcode == 0x9c:
            return IFGE()
        elif opcode == 0x9d:
            return IFGT()
        elif opcode == 0x9e:
            return IFLE()

        elif opcode == 0xb2:
            return GET_STATIC()
        elif opcode == 0xb3:
            return PUT_STATIC()
        elif opcode == 0xb4:
            return GET_FIELD()
        elif opcode == 0xb5:
            return PUT_FIELD()

        elif opcode == 0xb6:
            return INVOKE_VIRTUAL()
        elif opcode == 0xb7:
            return INVOKE_SPECIAL()
        elif opcode == 0xbb:
            return NEW()

        elif opcode == 0xc0:
            return CHECK_CAST()
        elif opcode == 0xc1:
            return INSTANCE_OF()

        else:
            # print("Unsupported opcode: {0}!".format(hex(opcode)))
            raise RuntimeError("Unsupported opcode: {0}!".format(hex(opcode)))