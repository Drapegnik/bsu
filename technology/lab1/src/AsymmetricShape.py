#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.Shape import Shape


class AsymmetricShape(Shape):
    def __init__(self, location=None, border_color=None, bg_color=None, points=[]):
        Shape.__init__(self, location, border_color, bg_color)
        self.points = points

    @staticmethod
    def name():
        return 'Asymmetric Shape'

    def render(self, ):
        pass

    def get_points(self, ):
        pass

    def set_points(self, value):
        pass
