#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.Shape import Shape
from utils import get_distance


class Ellipse(Shape):
    def __init__(self, location=None, point2=None, point3=None, border_color=None, bg_color=None):
        Shape.__init__(self, location, border_color, bg_color, [point2, point3])
        self.radx = get_distance(self.get_location(), self.points[0])
        if point3 is not None:
            self.rady = get_distance(self.get_location(), self.points[1])

    @staticmethod
    def name():
        return 'Ellipse'

    def render(self, qp):
        qp.setPen(self.get_pen())
        qp.setBrush(self.get_bg_color())
        qp.drawEllipse(self.get_location(), self.radx, self.rady)
