#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.Figure import Figure


class Shape(Figure):
    def __init__(self, location=None, border_color=None, bg_color=None):
        Figure.__init__(self, location, border_color)
        self.bg_color = bg_color

    def render(self, qp):
        pass

    def get_bg_color(self):
        return self.bg_color

    def set_bg_color(self, value):
        self.bg_color = value
