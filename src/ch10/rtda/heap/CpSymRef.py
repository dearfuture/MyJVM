#!/usr/bin/env python
# encoding: utf-8

class SymRef:
    def __init__(self):
        # 用于存放符号引用所在的运行时常量池
        self.rt_constant_pool = None
        # 类的完全限定名
        self.class_name = ""
        # 缓存解析后的类
        self._class = None

    def resolved_class(self):
        if self._class is None:
            self.resolve_class_ref()

        return self._class

    def resolve_class_ref(self):
        d = self.rt_constant_pool.clazz
        c = d.loader.load_class(self.class_name)
        if c.is_accessible_to(d):
            self._class = c
        else:
            raise RuntimeError("java.lang.IllegalAccessError")




