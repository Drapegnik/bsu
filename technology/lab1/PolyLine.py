#!/usr/bin/python
# -*- coding: utf-8 -*-


class PolyLine:
    def __init__(self, segments=[]):
        self.segments = segments

    def render(self):
        pass

    def get_segments(self):
        return self.segments

    def set_segments(self, value):
        self.segments = value
