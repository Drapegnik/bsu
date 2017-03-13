#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen

from src.Figure import Figure
from utils import midpoint


class LineSegment(Figure):
    def __init__(self, start_point=None, end_point=None, border_color=Qt.black):
        location = midpoint(start_point, end_point)
        Figure.__init__(self, location, border_color)
        self.start_point = start_point
        self.end_point = end_point

    @staticmethod
    def name():
        return 'Segment'

    def render(self, qp):
        pen = QPen(self.border_color, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.start_point, self.end_point)

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, value):
        self.start_point = value

    def get_end_point(self):
        return self.end_point

    def set_end_point(self, value):
        self.end_point = value
