#!/usr/bin/env python
# encoding: utf-8
from instructions.comparsions.Ifcond import IFEQ, IFNE, IFLT, IFGE, IFGT, IFLE
from instructions.comparsions.Ificmp import IF_ICMPLE
from instructions.comparsions.Lcmp import LCMP
from instructions.constants.Const import ICONST_0, ICONST_1, ICONST_M1, ACONST_NULL, LCONST_1, ICONST_2, ICONST_3, \
    LCONST_0, ICONST_4, ICONST_5
from instructions.constants.Ipush import BIPUSH
from instructions.constants.Ldc import LDC_W, LDC, LDC2_W
from instructions.constants.Nop import NOP
from instructions.control.Goto import GOTO
from instructions.control.Return import ARETURN, RETURN, IRETURN, LRETURN, DRETURN, FRETURN
from instructions.loads.Aload import ALOAD, ALOAD_1, ALOAD_2, ALOAD_3, ALOAD_0
from instructions.loads.Iload import ILOAD_2, ILOAD_1, ILOAD_3, ILOAD
from instructions.loads.Lload import LLOAD_0, LLOAD_1, LLOAD_2, LLOAD_3, LLOAD
from instructions.math.Add import IADD, LADD
from instructions.math.Iinc import IINC
from instructions.math.Sub import LSUB
from instructions.references.CheckCast import CHECK_CAST
from instructions.references.GetField import GET_FIELD
from instructions.references.GetStatic import GET_STATIC
from instructions.references.InstanceOf import INSTANCE_OF
from instructions.references.InvokeInterface import INVOKE_INTERFACE
from instructions.references.InvokeSpecial import INVOKE_SPECIAL
from instructions.references.InvokeStatic import INVOKE_STATIC
from instructions.references.InvokeVirtual import INVOKE_VIRTUAL
from instructions.references.New import NEW
from instructions.references.PutField import PUT_FIELD
from instructions.references.PutStatic import PUT_STATIC
from instructions.stack.Dup import DUP
from instructions.stores.Astore import ASTORE, ASTORE_1, ASTORE_2, ASTORE_3, ASTORE_0
from instructions.stores.Istore import ISTORE_1, ISTORE_2, ISTORE_3
from instructions.stores.Lstore import LSTORE_1, LSTORE_0, LSTORE_2, LSTORE_3


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
        elif opcode == 0x05:
            return ICONST_2()
        elif opcode == 0x06:
            return ICONST_3()
        elif opcode == 0x07:
            return ICONST_4()
        elif opcode == 0x08:
            return ICONST_5()

        elif opcode == 0x09:
            return LCONST_0()
        elif opcode == 0x0a:
            return LCONST_1()


        elif opcode == 0x10:
            return BIPUSH()
        elif opcode == 0x12:
            return LDC()
        elif opcode == 0x13:
            return LDC_W()
        elif opcode == 0x14:
            return LDC2_W()

        elif opcode == 0x15:
            return ILOAD()
        elif opcode == 0x16:
            return LLOAD()
        # elif opcode == 0x17:
        #     return FLOAD()
        # elif opcode == 0x18:
        #     return DLOAD()
        elif opcode == 0x19:
            return ALOAD()

        elif opcode == 0x1b:
            return ILOAD_1()
        elif opcode == 0x1c:
            return ILOAD_2()
        elif opcode == 0x1d:
            return ILOAD_3()

        elif opcode == 0x1e:
            return LLOAD_0()
        elif opcode == 0x1f:
            return LLOAD_1()
        elif opcode == 0x20:
            return LLOAD_2()
        elif opcode == 0x21:
            return LLOAD_3()

        elif opcode == 0x2a:
            return ALOAD_0()
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
        elif opcode == 0x3d:
            return ISTORE_2()
        elif opcode == 0x3e:
            return ISTORE_3()

        elif opcode == 0x3f:
            return LSTORE_0()
        elif opcode == 0x40:
            return LSTORE_1()
        elif opcode == 0x41:
            return LSTORE_2()
        elif opcode == 0x42:
            return LSTORE_3()

        elif opcode == 0x4b:
            return ASTORE_0()
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
        elif opcode == 0x61:
            return LADD()
        elif opcode == 0x65:
            return LSUB()

        elif opcode == 0x84:
            return IINC()

        elif opcode == 0xa4:
            return IF_ICMPLE()
        elif opcode == 0xa7:
            return GOTO()

        elif opcode == 0x94:
            return LCMP()
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

        elif opcode == 0xac:
            return IRETURN()
        elif opcode == 0xad:
            return LRETURN()
        elif opcode == 0xae:
            return FRETURN()
        elif opcode == 0xaf:
            return DRETURN()
        elif opcode == 0xb0:
            return ARETURN()
        elif opcode == 0xb1:
            return RETURN()

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
        elif opcode == 0xb8:
            return INVOKE_STATIC()
        elif opcode == 0xb9:
            return INVOKE_INTERFACE()

        elif opcode == 0xbb:
            return NEW()

        elif opcode == 0xc0:
            return CHECK_CAST()
        elif opcode == 0xc1:
            return INSTANCE_OF()

        else:
            # print("Unsupported opcode: {0}!".format(hex(opcode)))
            raise RuntimeError("Unsupported opcode: {0}!".format(hex(opcode)))