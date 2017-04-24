# coding=utf-8
from numpy import *
from numpy.linalg import *

inp = open('input2.txt', 'r')
out = open('output.txt', 'w')

A = []
n = 5
eps = 10 ** (-15)

for line in inp:  # читаем А
    temp = [float(x) for x in line.split()]
    A.append(temp)

a = array(A)
At = a.transpose()  # находим Аt
a = dot(At, a)  # перемножаем А на Аt, теперь А - симметрическая

out.write('A:\n {}\n'.format(a))

yk = ones(5)  # начальное приближеие
y = dot(a, yk)  # Y1
l = y[0] / yk[0]  # начальное лямбда
k = 1

while (True):  # итерацционный процесс
    yk = dot(a, y)
    lk = yk[0] / y[0]
    yk /= max(yk)
    if abs(lk - l) <= eps:
        break
    y = yk
    l = lk
    k += 1

p = [4.58801522, -7.82119475, 6.11344651, -2.15665219, 0.2685558]  # из Данилевского
out.write('lambdа:\n {}\n'.format(lk))
out.write('x:\n {}\n'.format(yk))
out.write('k:\n {}\n'.format(k))
out.write('p:\n {}\n'.format(p))

r = dot(a, yk) - lk * yk  # находим вектор невязки
out.write('r:\n {}\n'.format(r))
out.write('||r||:\n {}\n'.format(norm(r, 1)))

p.insert(0, -1)
r1 = sum(-(lk ** (n - i)) * p[i] for i in range(n + 1))  # считаем невязку собственного многочлена Pn(l)
out.write('Pn(l):\n {}\n'.format(r1))
out.write('eps:\n {}\n'.format(eps))
