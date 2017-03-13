#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget


class DrawArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setToolTip('This is a Draw Area!')
        self.show()

    def mousePressEvent(self, event):
        print(event.pos())
