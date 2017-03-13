#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPen

from src.LineSegment import LineSegment


class Ray(LineSegment):
    @staticmethod
    def name():
        return 'Ray'

    def render(self, qp):
        super().render(qp)

        pen = QPen(self.get_border_color())
        pen.setWidth(10)
        qp.setPen(pen)
        qp.drawPoint(self.get_end_point())
