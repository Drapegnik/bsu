# coding=utf-8
from numpy import *
from math import *

inp = open('input2.txt', 'r')
out = open('output.txt', 'w')

A, B = [], []
n, m = 5, 5


for line in inp:  # читаем А и b
    temp = [float(x) for x in line.split()]
    B.append(temp.pop())
    A.append(temp)

a = array(A)
At = a.transpose()  # находим Аt
b = array(B).transpose()

a, b = dot(At, a), dot(At, b)  # перемножаем А на Аt, теперь А - симметрическая

out.write('A:\n {}\n'.format(a))
out.write('b:\n {}\n'.format(b))

s, d = zeros((n, m)), zeros(n)

s[0][0] = sqrt(a[0][0])
d[0] = copysign(1, a[0][0])
for i in range(n):  # находим S и D по известным формулам
    val = a[i][i] - fsum([(s[k][i] ** 2) * d[k] for k in range(i)])
    d[i] = copysign(1, val)
    s[i][i] = sqrt(fabs(val))
    for j in range(i, n):
        s[i][j] = (a[i][j] - fsum([s[k][i] * d[k] * s[k][j] for k in range(i)])) / (s[i][i] * d[i])

out.write('S:\n {}\n'.format(s))
out.write('D:\n {}\n'.format(d))

det = prod([(s[i][i] ** 2) * d[i] for i in range(n)])  # вычисляем определитель

out.write('det:\n {} ({})\n'.format(det, sqrt(det)))

y = zeros(n)
y[0] = b[0] / s[0][0]  # находим y
for i in range(1, n):
    y[i] = (b[i] - fsum([s[k][i] * y[k] for k in range(i)])) / s[i][i]
out.write('y:\n {}\n'.format(y))

x = zeros(n)
x[n - 1] = y[n - 1] / s[n - 1][n - 1]  # находим x
for i in range(n - 2, -1, -1):
    x[i] = (y[i] - fsum([s[i][k] * x[k] for k in range(i + 1, n)])) / s[i][i]

out.write('x:\n {}\n'.format(x))

r1 = dot(A, x) - array(B)  # вычисляем невязку исходной
r2 = dot(a, x) - b.transpose()  # вычисляем невязку симетричной

out.write('r1:\n {}\n'.format(r1))
out.write('r2:\n {}\n'.format(r2))

out.write('||r1||:\n {}\n'.format(fsum([fabs(r1[i]) for i in range(n)])))
out.write('||r2||:\n {}\n'.format(fsum([fabs(r2[i]) for i in range(n)])))

inp.close()
out.close()
