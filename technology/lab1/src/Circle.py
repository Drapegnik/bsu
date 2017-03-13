#!/usr/bin/python
# -*- coding: utf-8 -*-

from RegularShape import RegularShape


class Circle(RegularShape):
    def __init__(self, location=None, point=None, border_color=None, bg_color=None):
        RegularShape.__init__(self, location, border_color, bg_color, [point])

    def render(self):
        pass
