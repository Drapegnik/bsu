import time

import numpy as np
from numpy import linalg as la

tol = 10.0 ** (-7)
h0 = 0.1
T = 1
EULER_ACCURACY = 1
RUNGE_KUTTA_ACCURACY = 4

A = 0
B = T

alpha = 0.8
sigma = 10
b = 8./3
r = 28

y0 = np.array([-8, 8, r - 1])
a = np.array([0, 1./2, 1./2, 1])
c = np.array([1./6, 2./6, 2./6, 1./6])


def f(y1, y2, y3):
    return np.array([
        -sigma*(y1 - y2),
        -y1*y3 + r*y1 - y2,
        y1*y2 - b*y3
    ])


def iterate(method, y, h, num=1):
    for i in range(num):
        y = method(y, h)
    return y


def euler(y, h):
    return y + h * f(*y.tolist())


def runge_kutta(y, h):
    k = np.array(f(*y.tolist()), ndmin=2)
    for j in range(1, 4):
        k = np.vstack((k, f(*(y + a[j] * h * k[j - 1]).tolist())))
    return y + h * np.dot(c, k)


def runge_estimate(yh, y2h, p):
    return np.abs(la.norm(yh - y2h) / (2 ** p - 1))


def get_new_step(h_old, err, p):
    delta = (tol / err) ** (1.0 / (p + 1))
    return delta, alpha * delta * h_old


def find_step(method, p, h):
    n = 0
    y = np.array(y0)
    great = True

    while great:
        y2h = iterate(method, y, 2 * h)
        yh = iterate(method, y, h, 2)
        err = runge_estimate(yh, y2h, p)

        great = err > tol
        n += 1

        if great:
            delta, h_new = get_new_step(h, err, p)
            if delta < 1:
                h = h_new
            else:
                y = y2h
                h = min(h_new, (B - A - 2 * h) / 2)
    return h, n


print 'solve Euler:'
t_s = time.time()

h_e, N = find_step(euler, EULER_ACCURACY, h0)
n = int((B - A) / h_e)
y_n = iterate(euler, np.array(y0), h_e, n)

t_f = time.time()

print '\ttol:\t{}'.format(tol)
print '\th:\t{}'.format(h_e)
print '\tn:\t{}'.format(n)
print '\tN:\t{}'.format(N)
print '\tyn:\t{}'.format(y_n)
print '\tt:\t{}s\n'.format(t_f - t_s)

print 'solve Runge-Kutta:'
t_s = time.time()

h_rk, N = find_step(runge_kutta, RUNGE_KUTTA_ACCURACY, h0)
n = int((B - A) / h_rk)
y_n = iterate(runge_kutta, np.array(y0), h_rk, n)

t_f = time.time()

print '\ttol:\t{}'.format(tol)
print '\th:\t{}'.format(h_rk)
print '\tn:\t{}'.format(n)
print '\tN:\t{}'.format(N)
print '\tyn:\t{}'.format(y_n)
print '\tt:\t{}s\n'.format(t_f - t_s)
