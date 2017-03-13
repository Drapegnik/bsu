#!/usr/bin/python3
# -*- coding: utf-8 -*-

from src.LineSegment import LineSegment
from utils import *


class Line(LineSegment):
    def __init__(self, start_point=None, end_point=None, border=None, border_color=None):
        line = get_line(start_point, end_point)
        start_point = QPoint(0.0001, get_y_from_x(line, 0.0001))
        end_point = QPoint(border.bottomRight().x(), get_y_from_x(line, border.bottomRight().x()))
        super().__init__(start_point, end_point, border_color)

    @staticmethod
    def name():
        return 'Line'