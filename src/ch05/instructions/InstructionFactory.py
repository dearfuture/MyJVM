#!/usr/bin/env python
# encoding: utf-8
from instructions.comparsions.Ificmp import IF_ICMPLE
from instructions.constants.Const import ICONST_0, ICONST_1, ICONST_M1, ACONST_NULL
from instructions.constants.Ipush import BIPUSH
from instructions.constants.Nop import NOP
from instructions.control.Goto import Goto
from instructions.loads.Iload import ILOAD_2, ILOAD_1
from instructions.math.Add import IAdd
from instructions.math.Iinc import IINC
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
        elif opcode == 0x1b:
            return ILOAD_1()
        elif opcode == 0x1c:
            return ILOAD_2()

        elif opcode == 0x3c:
            return ISTORE_1()
        elif opcode == 0x3d:
            return ISTORE_2()

        elif opcode == 0x84:
            return IINC()

        elif opcode == 0xa4:
            return IF_ICMPLE()
        elif opcode == 0xa7:
            return Goto()

        elif opcode == 0x60:
            return IAdd()

        else:
            # print("Unsupported opcode: {0}!".format(hex(opcode)))
            raise RuntimeError("Unsupported opcode: {0}!".format(hex(opcode)))