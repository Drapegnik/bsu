#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPen

from src.LineSegment import LineSegment


class Ray(LineSegment):
    @staticmethod
    def name():
        return 'Ray'

    def render(self, qp):
        super().render(qp)

        qp.setPen(QPen(self.get_border_color(), 10))
        qp.drawPoint(self.get_end_point())
