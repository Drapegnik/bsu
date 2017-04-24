# coding=utf-8
from numpy import *
from numpy.linalg import *

inp = open('input2.txt', 'r')
out = open('output.txt', 'w')

A, f = [], []
n, m = 5, 5
E = identity(n)
eps = 10 ** (-5)

for line in inp:  # читаем А и b
    temp = [float(x) for x in line.split()]
    f.append(temp.pop())
    A.append(temp)

a = array(A)
At = a.transpose()  # находим Аt
b = array(f).transpose()

a, b = dot(At, a), dot(At, b)  # перемножаем А на Аt, теперь А - симметрическая, то же самое с b

out.write('A:\n {}\n'.format(a))
out.write('b:\n {}\n'.format(b))

xk = b / diag(a)  # начальное приближение
x = zeros(n)
k = 0

while True:  # итерационный процесс
    rk = dot(a, xk) - b  # считаем rk
    x = xk - dot(rk, dot(rk, rk) / dot(dot(a, rk), rk))
    if abs(norm(x, inf) - norm(xk, inf)) < eps:
        break
    xk = x
    k += 1

out.write('x:\n {}\n'.format(x))
out.write('k:\n {}\n'.format(k))

r = dot(A, x) - f  # находим вектор невязки

out.write('r:\n {}\n'.format(r))
out.write('||r||:\n {}\n'.format(norm(r, 1)))
out.write('eps:\n {}\n'.format(eps))
