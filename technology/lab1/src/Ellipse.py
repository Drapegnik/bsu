#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.SymmetricShape import SymmetricShape


class Ellipse(SymmetricShape):
    def __init__(self, location=None, point2=None, point3=None, border_color=None, bg_color=None):
        SymmetricShape.__init__(self, location, border_color, bg_color, [point2, point3])

    @staticmethod
    def name():
        return 'Ellipse'

    def render(self):
        pass
