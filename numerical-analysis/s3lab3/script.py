# coding=utf-8
from numpy import *
from math import *

inp = open('input.txt', 'r')
out = open('output.txt', 'w')

A, f, a, b, c = [], [], [], [], []
n, m = 5, 5

for line in inp:  # читаем А и b
    temp = [float(x) for x in line.split()]
    f.append(temp.pop())
    A.append(temp)

for i in range(n):  # переименовываем переменный главной диагонали
    c.append(A[i][i])

a.append(0)
for i in range(n - 1):
    a.append(-A[i + 1][i])  # переименовываем переменный верхней диагонали
    b.append(-A[i][i + 1])  # переименовываем переменный нижней диагонали
b.append(0)

alp, bet, x = zeros(n), zeros(n), zeros(n)

alp[n - 1] = a[n - 1] / c[n - 1]  # вычисляем начальные альфа и бета
bet[n - 1] = f[n - 1] / c[n - 1]

for i in range(n - 2, 0, -1):
    alp[i] = a[i] / (c[i] - b[i] * alp[i + 1])
    bet[i] = (bet[i + 1] * b[i] + f[i]) / (c[i] - b[i] * alp[i + 1])

x[0] = (f[0] + bet[1] * b[0]) / (c[0] - alp[1] * b[0])  # вычисляем первый x

for i in range(1, n):
    x[i] = alp[i] * x[i - 1] + bet[i]

det = prod([c[i] - a[i] * alp[i] for i in range(n)])  # вычисление определителя

r = dot(A, x) - f  # вычисление вектора невязки

out.write('A:\n {}\n'.format(A))
out.write('a:\n {}\n'.format(a))
out.write('b:\n {}\n'.format(b))
out.write('c:\n {}\n'.format(c))
out.write('f:\n {}\n'.format(f))
out.write('alpha:\n {}\n'.format(alp))
out.write('beta:\n {}\n'.format(bet))
out.write('x:\n {}\n'.format(x))
out.write('r:\n {}\n'.format(r))
out.write('det:\n {}\n'.format(det))
out.write('||r||:\n {}\n'.format(fsum([fabs(r[i]) for i in range(n)])))
