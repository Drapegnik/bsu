#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.Figure import Figure


class LineSegment(Figure):
    def __init__(self, location=None, border_color=None, start_point=None, end_point=None):
        Figure.__init__(self, location, border_color)
        self.start_point = start_point
        self.end_point = end_point

    @staticmethod
    def name():
        return 'Segment'

    def render(self):
        pass

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, value):
        self.start_point = value

    def get_end_point(self):
        return self.end_point

    def set_end_point(self, value):
        self.end_point = value
