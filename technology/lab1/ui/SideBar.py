#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import partial

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from src import *
from src import shapes
from ui.QColorButton import QColorButton


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.active = None
        self.set_bg_color(QColor('lightgray'))
        self.radios = self.get_radions()
        self.num_btn = QPushButton('Set num', self)
        self.reset_btn = QPushButton('Reset', self)
        self.border_color_btn = QColorButton()
        self.bg_color_btn = QColorButton()
        self.render_buttons()
        self.show()

    @staticmethod
    def get_radions():
        return list(map(lambda cls: QRadioButton(cls.name()), shapes))

    def render_buttons(self):
        layout = QVBoxLayout()
        self.radios[0].setChecked(True)
        self.parent.active = self.radios[0].text()
        self.parent.num = 3
        layout.addStretch(0)
        layout.addWidget(self.num_btn)
        layout.addWidget(self.reset_btn)
        layout.addWidget(QLabel('Border color:', self))
        layout.addWidget(self.border_color_btn)
        layout.addWidget(QLabel('Bg color:', self))
        layout.addWidget(self.bg_color_btn)
        layout.addWidget(QLabel('Figure:', self))

        for item in self.radios:
            layout.addWidget(item)

        for i in range(len(self.radios)):
            self.radios[i].toggled.connect(partial(self.on_select, self.radios[i]))
        self.num_btn.clicked.connect(lambda: self.show_dialog(self.parent.active))
        self.reset_btn.clicked.connect(lambda: self.parent.draw_area.reset())

        self.setLayout(layout)

    def on_select(self, radio):
        if radio.isChecked():
            self.show_dialog(radio.text())
            self.parent.active = radio.text()

    def set_bg_color(self, color=QColor('white')):
        p = self.palette()
        p.setColor(self.backgroundRole(), color)
        self.setPalette(p)
        self.setAutoFillBackground(True)

    def show_dialog(self, active_name):
        ok, min, step = False, 3, 1
        if active_name in [PolyLine.name(), AsymmetricShape.name(), RegularShape.name(), SymmetricShape.name()]:
            if active_name == SymmetricShape.name():
                min, step = 4, 2
            num, ok = QInputDialog.getInt(self, 'points dialog', 'enter a number of points', min=min, step=step)
        if not ok:
            num = 3
        self.parent.num = num
