#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PolyLine:
    def __init__(self, segments=[]):
        self.segments = segments

    @staticmethod
    def name():
        return 'Poly Line'

    def render(self, qp):
        for seg in self.segments:
            seg.render(qp)

    def add_segment(self, value):
        self.segments.append(value)

    def get_segments(self):
        return self.segments

    def set_segments(self, value):
        self.segments = value
