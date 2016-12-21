import time

import numpy as np
from numpy import linalg as la

tol = 0.000001
h0 = 0.01
T = 0.1
EULER_ACCURACY = 1
RUNGE_KUTTA_ACCURACY = 4

A = 0
B = T

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


def euler(start, finish, h):
    n = int((finish - start)/h)
    y = np.array(y0, ndmin=2)
    for i in range(n):
        y = np.vstack((y, y[i] + h*f(*y[i].tolist())))

    return y[n]


def runge_estimate(yh, y2h, p):
    print yh
    return la.norm(np.abs(yh) - np.abs(y2h), -1)/(2**p - 1)


def runge_kutta(start, finish, h):
    n = int((finish - start)/h)
    y = np.array(y0, ndmin=2)
    for i in range(n):
        k = np.array(f(*y[i].tolist()), ndmin=2)
        for j in range(1, 4):
            k = np.vstack((k, f(*(y[i] + a[j]*h*k[j - 1]).tolist())))
        y = np.vstack((y, y[i] + h*f(*y[i].tolist())))

    return y[n]


print 'solve Euler'
h_e = h0

t_s = time.time()
N = 0
while runge_estimate(euler(A, B, h_e), euler(A, B, 2*h_e), EULER_ACCURACY) > tol:
    h_e /= 2
    N += 1
t_f = time.time()

print 'h={}'.format(h_e)
print 'n={}'.format(int((B - A)/h_e))
print 'N={}'.format(N)
print 't={}s\n'.format(t_f - t_s)

print 'solve Runge-Kutta'
h_rk = h0

t_s = time.time()
N = 0
while runge_estimate(runge_kutta(A, B, h_rk), runge_kutta(A, B, 2*h_rk), RUNGE_KUTTA_ACCURACY) > tol:
    h_rk /= 2
    N += 1
t_f = time.time()

print 'h={}'.format(h_rk)
print 'n={}'.format(int((B - A)/h_rk))
print 'N={}'.format(N)
print 't={}s\n'.format(t_f - t_s)
