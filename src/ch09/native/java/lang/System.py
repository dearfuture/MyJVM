#!/usr/bin/env python
# encoding: utf-8
from native import Registry
from rtda.Frame import Frame

def arraycopy(frame: Frame):
    vars = frame.local_vars
    src = vars.get_ref(0)
    src_pos = vars.get_numeric(1)
    dest = vars.get_ref(2)
    dest_pos = vars.get_numeric(3)
    length = vars.get_numeric(4)

    if src is None or dest is None:
        raise RuntimeError("java.lang.NullPointerException")

    # TODO check

    for i in range(length):
        dest.data[dest_pos + i] = src.data[src_pos + i]

    return


Registry.register("java/lang/System", "arraycopy", "(Ljava/lang/Object;ILjava/lang/Object;II)V", arraycopy)