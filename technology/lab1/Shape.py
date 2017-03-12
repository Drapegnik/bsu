#!/usr/bin/python
#-*- coding: utf-8 -*-

from Figure import Figure
from AsymmetricShape import AsymmetricShape

class Shape(Figure, AsymmetricShape):
    def __init__(self):
        self.bg_color = None

    def render(self, ):
        pass

    def get_bg_color(self, ):
        pass

    def set_bg_color(self, value):
        pass

