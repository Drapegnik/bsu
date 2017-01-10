from math import sin

import numpy as np
from mpi4py import MPI


class Task:
    f = staticmethod(lambda x, y: x * y)
    f_left = f1 = staticmethod(lambda y: y ** 2)
    f_right = f2 = staticmethod(lambda y: sin(y))
    f_bottom = f3 = staticmethod(lambda x: x ** 3)
    f_top = f4 = staticmethod(lambda x: x ** 2)


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return '({0:.2f}, {1:.2f})'.format(self.x, self.y)


class Index:
    def __init__(self, rows, rows_start, cols, cols_start):
        self.rows, self.rows_start, self.cols, self.cols_start = rows, rows_start, cols, cols_start


class Region:
    def __init__(self, top=0, right=0, bottom=0, left=0):
        self.top, self.right, self.bottom, self.left = top, right, bottom, left

    def __repr__(self):
        return '{' \
               + 't: {0}, r: {1}, b: {2}, l: {3}'.format(self.top, self.right, self.bottom, self.left) \
               + '}'


class ProcSquare:
    def __init__(self, full_region, region, left_top, step_x, step_y):
        self.full_region, self.region, self.left_top, self.step_x, self.step_y = full_region, region, left_top, step_x, step_y
        self.rows = region.bottom - region.top
        self.cols = region.right - region.left
        self.calc_region = Region(
            top=int(region.top == full_region.top),
            left=int(region.left == full_region.left),
            right=self.cols - int(region.right == full_region.right),
            bottom=self.rows - int(region.bottom == full_region.bottom)
        )
        self.diff = 0.0

        if self.rows > 0 and self.cols > 0:
            self.top_border = np.zeros(self.cols, dtype=np.float64)
            self.left_border = np.zeros(self.rows, dtype=np.float64)
            self.bottom_border = np.zeros(self.cols, dtype=np.float64)
            self.right_border = np.zeros(self.rows, dtype=np.float64)

            self.sqr_step_x = self.step_x * self.step_x
            self.sqr_step_y = self.step_y * self.step_y
            self.weight = 1. / (2 * (1. / self.sqr_step_x + 1. / self.sqr_step_y))

            if self.region.top == self.full_region.top:
                for j in range(self.cols):
                    self.set(0, j, Task.f_top(left_top.x + step_x * j))
            else:
                self.neighbor_top_border = np.zeros(self.cols, dtype=np.float64)

            if region.bottom == full_region.bottom:
                for j in range(self.cols):
                    self.set(self.rows - 1, j, Task.f_bottom(left_top.x + step_x * j))
            else:
                self.neighbor_bottom_border = np.zeros(self.cols, dtype=np.float64)

            if region.left == full_region.left:
                for i in range(self.rows):
                    self.set(i, 0, Task.f_left(left_top.y + step_y * i))
            else:
                self.neighbor_left_border = np.zeros(self.rows, dtype=np.float64)

            if region.right == full_region.right:
                for i in range(self.rows):
                    self.set(i, self.cols - 1, Task.f_right(left_top.y + step_y * i))
            else:
                self.neighbor_right_border = np.zeros(self.rows, dtype=np.float64)

        if self.rows > 2 and self.cols > 2:
            self.inner_lines = []
            for i in range(self.rows - 2):
                self.inner_lines.append(np.zeros(self.cols - 2, dtype=np.float64))

    def get(self, i, j):
        if j == -1:
            return self.neighbor_left_border[i]
        elif j == self.cols:
            return self.neighbor_right_border[i]
        elif i == -1:
            return self.neighbor_top_border[j]
        elif i == self.rows:
            return self.neighbor_bottom_border[j]
        elif j == 0:
            return self.left_border[i]
        elif j == self.cols - 1:
            return self.right_border[i]
        elif i == 0:
            return self.top_border[j]
        elif i == self.rows - 1:
            return self.bottom_border[j]
        else:
            return self.inner_lines[i - 1][j - 1]

    def set(self, i, j, val):
        if j == -1:
            self.neighbor_left_border[i] = val
        elif j == self.cols:
            self.neighbor_right_border[i] = val
        elif i == -1:
            self.neighbor_top_border[j] = val
        elif i == self.rows:
            self.neighbor_bottom_border[j] = val
        else:
            if j == 0:
                self.left_border[i] = val

            if j == self.cols - 1:
                self.right_border[i] = val

            if i == 0:
                self.top_border[j] = val

            if i == self.rows - 1:
                self.bottom_border[j] = val

            if (0 < i < self.rows - 1) and (0 < j < self.cols - 1):
                self.inner_lines[i - 1][j - 1] = val

    def exch(self, comm):
        left, right = comm.Shift(1, 1)
        top, bottom = comm.Shift(0, 1)

        if top != MPI.PROC_NULL:
            comm.send(self.top_border, dest=top)

        if bottom != MPI.PROC_NULL:
            self.neighbor_bottom_border = comm.recv(source=bottom)

        if bottom != MPI.PROC_NULL:
            comm.send(self.bottom_border, dest=bottom)

        if top != MPI.PROC_NULL:
            self.neighbor_top_border = comm.recv(source=top)

        if right != MPI.PROC_NULL:
            comm.send(self.right_border, dest=right)

        if left != MPI.PROC_NULL:
            self.neighbor_left_border = comm.recv(source=left)

        if left != MPI.PROC_NULL:
            comm.send(self.left_border, dest=left)

        if right != MPI.PROC_NULL:
            self.neighbor_right_border = comm.recv(source=right)

        comm.barrier()

    def calc(self):
        self.diff = 0.0

        for i in range(self.calc_region.top, self.calc_region.bottom):
            for j in range(self.calc_region.left, self.calc_region.right):
                x = self.left_top.x + j * self.step_x
                y = self.left_top.y + i * self.step_y
                val = self.weight * (
                    (self.get(i + 1, j) + self.get(i - 1, j)) / self.sqr_step_x +
                    (self.get(i, j + 1) + self.get(i, j - 1)) / self.sqr_step_y -
                    Task.f(x, y)
                )
                self.diff = max(self.diff, abs(self.get(i, j) - val))
                self.set(i, j, val=val)

    def data(self):
        temp = np.zeros(self.cols * self.rows, dtype=np.float64)

        for i in range(self.rows):
            for j in range(self.cols):
                temp[i * self.cols + j] = self.get(i, j)

        return temp
