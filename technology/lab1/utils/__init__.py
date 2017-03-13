#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import QPoint


def midpoint(p1, p2):
    return QPoint((p1.x() + p2.x())/2, (p1.y() + p2.y())/2)


def get_line(p1, p2):
    return [p1.y() - p2.y(), p2.x() - p1.x(), p1.x()*p2.y() - p2.x()*p1.y()]


def get_perpendicular_line(line, p):
    return [-line[1], line[0], line[1]*p.x() - line[0]*p.y()]


def get_y_from_x(line, x):
    return -(line[0]*x + line[2])/line[1]
