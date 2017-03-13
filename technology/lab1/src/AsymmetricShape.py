#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPolygon

from src.Shape import Shape


class AsymmetricShape(Shape):
    def __init__(self, points=[], border_color=None, bg_color=None, location=None):
        Shape.__init__(self, location, border_color, bg_color, points)

    @staticmethod
    def name():
        return 'Asymmetric Shape'

    def render(self, qp):
        qp.setPen(self.get_pen())
        qp.drawPolygon(QPolygon(self.points))
