#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QWidget

from src import *


class DrawArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setToolTip('This is a Draw Area!')
        self.points = []
        self.figures = []
        self.moving = False
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_points(qp)
        self.draw_figures(qp)
        qp.end()

    def draw_points(self, qp):
        pen = QPen(Qt.red)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(5)
        qp.setPen(pen)

        for point in self.points:
            qp.drawPoint(point)

    def draw_figures(self, qp):
        for fig in self.figures:
            fig.render(qp)

    def mousePressEvent(self, event):
        if not self.moving:
            self.points = []
            self.update()

    def mouseMoveEvent(self, event):
        if not self.moving:
            self.points = []
            self.points.append(event.pos())
            self.update()
            self.moving = True
            # print('move')

    def mouseReleaseEvent(self, event):
        if self.moving:
            self.points.append(event.pos())
            if len(self.points) == 2:
                if self.parent.active == LineSegment.name():
                    self.figures.append(LineSegment(*self.points))
                elif self.parent.active == Ray.name():
                    self.figures.append(Ray(*self.points))
                elif self.parent.active == Line.name():
                    self.figures.append(Line(*self.points, self.geometry()))
                elif self.parent.active == Circle.name():
                    print('circle')
            self.moving = False
            self.update()
