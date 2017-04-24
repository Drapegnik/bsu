import sys

import numpy as np

A = -2.0
B = 2.0
n = 5
x = np.arange(A, B + 0.1, (B - A) / n)
F_SECOND_DER = -0.0239496  # f''(a)=f''(b)


def f(x):
    return float(x * (3 ** x + 1) ** (-1))


def get_c():
    rhs = [3 * ((f(x[i]) - f(x[i - 1])) / (x[i] - x[i - 1]) - (f(x[i - 1]) - f(x[i - 2])) / (x[i - 1] - x[i - 2]))
           for i in range(2, n + 1)]
    rhs.insert(0, F_SECOND_DER)
    rhs.append(F_SECOND_DER)

    lhs = np.zeros((n + 1, n + 1), float)
    np.fill_diagonal(lhs, [1.0] + [2 * (x[i] - x[i - 2]) for i in range(2, n + 1)] + [1.0])  # main diag
    lhs += np.diagflat([x[i] - x[i - 1] for i in range(1, n + 1)], 1)  # upper diag
    lhs += np.diagflat([x[i - 1] - x[i - 2] for i in range(2, n + 2)], -1)  # lower diag
    return np.linalg.solve(lhs, rhs)


def get_d(c):
    return [(c[i + 1] - c[i]) / (3 * (x[i] - x[i - 1])) for i in range(1, n)] + [-c[n] / (3 * (x[n] - x[n - 1]))]


def get_b(c):
    return [(f(x[i]) - f(x[i - 1])) / (x[i] - x[i - 1]) - (1 / 3) * (x[i] - x[i - 1]) * (c[i + 1] + 2 * c[i])
            for i in range(1, n)] + [(f(B) - f(x[n - 1])) / (x[n] - x[n - 1]) - 2 / 3 * c[n] * (x[n] - x[n - 1])]


def get_a():
    return [f(x[i - 1]) for i in range(1, n + 1)]


def spline(x0, i):
    return a[i] + b[i] * (x0 - x[i]) + c[i] * (x0 - x[i]) ** 2 + d[i] * (x0 - x[i]) ** 3


def accuracy():
    return [abs(f((x[i] + x[i - 1]) / 2) - spline((x[i] + x[i - 1]) / 2, i - 1)) for i in range(1, n + 1)]


def sign_print(el, val):
    sys.stdout.write(('{0:.' + str(val) + 'g}').format(el) + ', ')


def out(k, v):
    sys.stdout.write(k + ': [')
    map(sign_print, v, [3] * len(v))
    sys.stdout.write(']\n')


c = get_c()
a = get_a()
b = get_b(c)
d = get_d(c)

map(out, ('a', 'b', 'c', 'd'), (a, b, c, d))
sys.stdout.write('r: ')
map(sign_print, accuracy(), [1] * len(accuracy()))
