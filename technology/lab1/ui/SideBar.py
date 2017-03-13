#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor

from PyQt5.QtWidgets import QWidget


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('lightgray'))
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.show()

    def mousePressEvent(self, event):
        print(event.pos())
