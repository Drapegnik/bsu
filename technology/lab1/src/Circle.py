#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.Ellipse import Ellipse


class Circle(Ellipse):
    def __init__(self, location=None, point=None, border_color=None, bg_color=None):
        Ellipse.__init__(self, location, point, None, border_color, bg_color)
        self.rady = self.radx

    @staticmethod
    def name():
        return 'Circle'
