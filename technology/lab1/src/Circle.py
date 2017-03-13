#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.RegularShape import RegularShape


class Circle(RegularShape):
    def __init__(self, location=None, point=None, border_color=None, bg_color=None):
        RegularShape.__init__(self, location, border_color, bg_color, [point])

    @staticmethod
    def name():
        return 'Circle'

    def render(self):
        pass
