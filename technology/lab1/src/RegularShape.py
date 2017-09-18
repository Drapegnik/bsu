#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, sin, pi, atan

from PyQt5.QtCore import QPoint

from src.AsymmetricShape import AsymmetricShape
from utils import get_distance


class RegularShape(AsymmetricShape):
    def __init__(self, location=None, points=None, num=3, border_color=None, bg_color=None):
        super().__init__(points, border_color, bg_color, location)
        self._count_points(num)

    def _count_points(self, num):
        r = get_distance(self.points[0], self.get_location())
        alpha = atan((self.points[0].y() - self.get_location().y())/(self.points[0].x() - self.get_location().x()))
        for i in range(1, num):
            x = r*cos(2.0*pi*i/num + alpha) + self.get_location().x()
            y = r*sin(2.0*pi*i/num + alpha) + self.get_location().y()
            self.points.append(QPoint(x, y))

    @staticmethod
    def name():
        return 'Regular Shape'
