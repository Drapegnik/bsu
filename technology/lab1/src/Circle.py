#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen

from src.RegularShape import RegularShape


class Circle(RegularShape):
    def __init__(self, location=None, point=None, border_color=None, bg_color=None):
        RegularShape.__init__(self, location, border_color, bg_color, [point])
        self.radx = math.hypot(
            self.points[0].x() - self.get_location().x(),
            self.points[0].y() - self.get_location().y()
        )

    @staticmethod
    def name():
        return 'Circle'

    def render(self, qp):
        pen = QPen(self.get_border_color(), 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(self.get_bg_color())
        qp.drawEllipse(self.get_location(), self.radx, self.radx)
