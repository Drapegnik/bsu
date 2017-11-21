#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.RegularShape import RegularShape


class SymmetricShape(RegularShape):
    # def _count_points(self, num):
    #     line = get_line(self.points[0], self.points[1])

    @staticmethod
    def name():
        return 'Symmetric Shape'
