#!/usr/bin/env python
# encoding: utf-8
from rtda.Object import Object


class Slot:
    # 存放数字
    # num: int/float/long/double
    # 存放引用
    # ref: Object

    def __init__(self):
        self.num = 0
        self.ref = None

    def __str__(self):
        return "num:{0} ref:{1}".format(self.num, self.ref)