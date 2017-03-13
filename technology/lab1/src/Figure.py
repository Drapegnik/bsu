#!/usr/bin/python
# -*- coding: utf-8 -*-


class Figure:
    def __init__(self, location=None, border_color=None):
        self.location = location
        self.border_color = border_color

    def render(self, qp):
        pass

    def get_location(self):
        return self.location

    def set_location(self, value):
        self.location = value

    def get_border_color(self):
        return self.border_color

    def set_border_color(self, value):
        self.border_color = value
