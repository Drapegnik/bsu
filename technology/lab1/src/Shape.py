#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt

from src.Figure import Figure


class Shape(Figure):
    def __init__(self, location=None, border_color=None, bg_color=Qt.white, points=[]):
        Figure.__init__(self, location, border_color)
        self.bg_color = bg_color if bg_color else Qt.white
        self.points = points

    def render(self, qp):
        pass

    def get_bg_color(self):
        return self.bg_color

    def set_bg_color(self, value):
        self.bg_color = value

    def get_points(self):
        return self.points

    def set_points(self, value):
        self.points = value
