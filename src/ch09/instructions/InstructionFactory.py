#!/usr/bin/env python
# encoding: utf-8
from instructions.comparsions.Ifacmp import IF_ACMPEQ, IF_ACMPNE
from instructions.comparsions.Ifcond import IFEQ, IFNE, IFLT, IFGE, IFGT, IFLE
from instructions.comparsions.Ificmp import IF_ICMPLE, IF_ICMPGT, IF_ICMPGE, IF_ICMPLT, IF_ICMPEQ, IF_ICMPNE
from instructions.comparsions.Lcmp import LCMP
from instructions.constants.Const import ICONST_0, ICONST_1, ICONST_M1, ACONST_NULL, LCONST_1, ICONST_2, ICONST_3, \
    LCONST_0, ICONST_4, ICONST_5
from instructions.constants.Ipush import BIPUSH, SIPUSH
from instructions.constants.Ldc import LDC_W, LDC, LDC2_W
from instructions.constants.Nop import NOP
from instructions.control.Goto import GOTO
from instructions.control.Return import ARETURN, RETURN, IRETURN, LRETURN, DRETURN, FRETURN
from instructions.convensions.I2x import I2L
from instructions.extended.IfNull import IF_NON_NULL, IF_NULL
from instructions.loads.Aload import ALOAD, ALOAD_1, ALOAD_2, ALOAD_3, ALOAD_0
from instructions.loads.Iload import ILOAD_2, ILOAD_1, ILOAD_3, ILOAD, ILOAD_0
from instructions.loads.Lload import LLOAD_0, LLOAD_1, LLOAD_2, LLOAD_3, LLOAD
from instructions.loads.Xaload import IALOAD, AALOAD, CALOAD
from instructions.math.Add import IADD, LADD
from instructions.math.And import IAND
from instructions.math.Iinc import IINC
from instructions.math.Mul import IMUL, LMUL
from instructions.math.Sh import IUSHR, ISHL, LSHL
from instructions.math.Sub import LSUB, ISUB
from instructions.references.AnewArray import ANEW_ARRAY
from instructions.references.ArrayLength import ARRAY_LENGTH
from instructions.references.CheckCast import CHECK_CAST
from instructions.references.GetField import GET_FIELD
from instructions.references.GetStatic import GET_STATIC
from instructions.references.InstanceOf import INSTANCE_OF
from instructions.references.InvokeInterface import INVOKE_INTERFACE
from instructions.references.InvokeNative import INVOKE_NATIVE
from instructions.references.InvokeSpecial import INVOKE_SPECIAL
from instructions.references.InvokeStatic import INVOKE_STATIC
from instructions.references.InvokeVirtual import INVOKE_VIRTUAL
from instructions.references.New import NEW
from instructions.references.NewArray import NEW_ARRAY
from instructions.references.PutField import PUT_FIELD
from instructions.references.PutStatic import PUT_STATIC
from instructions.stack.Dup import DUP
from instructions.stack.Pop import POP, POP2
from instructions.stores.Astore import ASTORE, ASTORE_1, ASTORE_2, ASTORE_3, ASTORE_0
from instructions.stores.Istore import ISTORE_1, ISTORE_2, ISTORE_3, ISTORE, ISTORE_0
from instructions.stores.Lstore import LSTORE_1, LSTORE_0, LSTORE_2, LSTORE_3
from instructions.stores.Xastore import IASTORE, CASTORE, SASTORE, AASTORE, BASTORE


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
        elif opcode == 0x11:
            return SIPUSH()
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

        elif opcode == 0x1a:
            return ILOAD_0()
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

        elif opcode == 0x2e:
            return IALOAD()
        elif opcode == 0x32:
            return AALOAD()
        elif opcode == 0x34:
            return CALOAD()
        elif opcode == 0x36:
            return ISTORE()

        elif opcode == 0x3a:
            return ASTORE()
        elif opcode == 0x3b:
            return ISTORE_0()
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

        elif opcode == 0x4f:
            return IASTORE()

        elif opcode == 0x53:
            return AASTORE()
        elif opcode == 0x54:
            return BASTORE()
        elif opcode == 0x55:
            return CASTORE()
        elif opcode == 0x56:
            return SASTORE()
        elif opcode == 0x57:
            return POP()
        elif opcode == 0x58:
            return POP2()
        elif opcode == 0x59:
            return DUP()

        elif opcode == 0x60:
            return IADD()
        elif opcode == 0x61:
            return LADD()
        elif opcode == 0x64:
            return ISUB()
        elif opcode == 0x65:
            return LSUB()

        elif opcode == 0x68:
            return IMUL()
        elif opcode == 0x69:
            return LMUL()

        elif opcode == 0x78:
            return ISHL()
        elif opcode == 0x79:
            return LSHL()
        elif opcode == 0x7c:
            return IUSHR()

        elif opcode == 0x7e:
            return IAND()
        elif opcode == 0x7f:
            return IAND()

        elif opcode == 0x84:
            return IINC()

        elif opcode == 0x85:
            return I2L()

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

        elif opcode == 0x9f:
            return IF_ICMPEQ()
        elif opcode == 0xa0:
            return IF_ICMPNE()
        elif opcode == 0xa1:
            return IF_ICMPLT()
        elif opcode == 0xa2:
            return IF_ICMPGE()
        elif opcode == 0xa3:
            return IF_ICMPGT()
        elif opcode == 0xa4:
            return IF_ICMPLE()
        elif opcode == 0xa5:
            return IF_ACMPEQ()
        elif opcode == 0xa6:
            return IF_ACMPNE()

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
        elif opcode == 0xbc:
            return NEW_ARRAY()
        elif opcode == 0xbd:
            return ANEW_ARRAY()
        elif opcode == 0xbe:
            return ARRAY_LENGTH()

        elif opcode == 0xc0:
            return CHECK_CAST()
        elif opcode == 0xc1:
            return INSTANCE_OF()

        elif opcode == 0xc6:
            return IF_NULL()
        elif opcode == 0xc7:
            return IF_NON_NULL()

        # 配合Method.inject_code_attribute(self, return_type)
        elif opcode == 0xfe:
            return INVOKE_NATIVE()

        else:
            # print("Unsupported opcode: {0}!".format(hex(opcode)))
            raise RuntimeError("Unsupported opcode: {0}!".format(hex(opcode)))