#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.Shape import Shape


class AsymmetricShape(Shape):
    def __init__(self, location=None, border_color=None, bg_color=None, points=[]):
        Shape.__init__(self, location, border_color, bg_color, points)

    @staticmethod
    def name():
        return 'Asymmetric Shape'

    def render(self, qp):
        pass