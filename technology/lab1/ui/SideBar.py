#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from src import *
from ui.QColorButton import QColorButton


class SideBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.active = None
        self.set_bg_color(QColor('lightgray'))
        self.radios = self.get_buttons()
        self.num_btn = QPushButton('Set num', self)
        self.border_color_btn = QColorButton()
        self.bg_color_btn = QColorButton()
        self.render_buttons()
        self.show()

    @staticmethod
    def get_buttons():
        segment = QRadioButton(LineSegment.name())
        line = QRadioButton(Line.name())
        ray = QRadioButton(Ray.name())
        polyline = QRadioButton(PolyLine.name())

        asym = QRadioButton(AsymmetricShape.name())
        reg = QRadioButton(RegularShape.name())
        sym = QRadioButton(SymmetricShape.name())

        circle = QRadioButton(Circle.name())
        ellipse = QRadioButton(Ellipse.name())
        return [segment, ray, line, polyline, asym, reg, sym, circle, ellipse]

    def render_buttons(self):
        layout = QVBoxLayout()
        self.radios[0].setChecked(True)
        self.parent.active = self.radios[0].text()
        self.parent.num = 3
        layout.addStretch(0)
        layout.addWidget(self.num_btn)
        layout.addWidget(QLabel('Border color:', self))
        layout.addWidget(self.border_color_btn)
        layout.addWidget(QLabel('Bg color:', self))
        layout.addWidget(self.bg_color_btn)
        layout.addWidget(QLabel('Figure:', self))

        for btn in self.radios:
            layout.addWidget(btn)

        self.radios[0].toggled.connect(lambda: self.on_select(self.radios[0]))
        self.radios[1].toggled.connect(lambda: self.on_select(self.radios[1]))
        self.radios[2].toggled.connect(lambda: self.on_select(self.radios[2]))
        self.radios[3].toggled.connect(lambda: self.on_select(self.radios[3]))
        self.radios[4].toggled.connect(lambda: self.on_select(self.radios[4]))
        self.radios[5].toggled.connect(lambda: self.on_select(self.radios[5]))
        self.radios[6].toggled.connect(lambda: self.on_select(self.radios[6]))
        self.radios[7].toggled.connect(lambda: self.on_select(self.radios[7]))
        self.radios[8].toggled.connect(lambda: self.on_select(self.radios[8]))
        self.num_btn.clicked.connect(lambda: self.show_dialog(self.parent.active))

        self.setLayout(layout)

    def on_select(self, btn):
        if btn.isChecked():
            self.show_dialog(btn.text())
            self.parent.active = btn.text()

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
