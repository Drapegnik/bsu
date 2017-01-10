# coding=utf-8
from numpy import *
from numpy.linalg import *
from sympy.solvers import solve
from sympy import Symbol

inp = open('input2.txt', 'r')
out = open('output.txt', 'w')

A = []
n = 5

for line in inp:  # читаем А
    temp = [float(x) for x in line.split()]
    A.append(temp)

a = array(A)
At = a.transpose()  # находим Аt
a = dot(At, a)  # перемножаем А на Аt, теперь А - симметрическая

out.write('A:\n {}\n'.format(a))

c = []
c.append([1, 0, 0, 0, 0])  # начальный Co
for i in range(1, n + 1):
    c.append(dot(a, c[i - 1]))  # рекурсивно вычисляем cn

C = array(c)  # копия С
cn = c.pop()  # выделяем столбец свободных членов nn
c = array(c).transpose()
for i in range(n):  # транспонируем матрицу коэфиццентов C
     c[i] = list(reversed(c[i]))

out.write('C:\n {}\n'.format(c))
out.write('cn:\n {}\n'.format(cn))

p = linalg.solve(c, cn)  # решаем систему C*p = cn
out.write('p:\n {}\n'.format(p))

x = Symbol('x')
Lambda = solve(x**5 - p[0] * x**4 - p[1] * x**3 - p[2] * x**2 - p[3] * x - p[4], x)  # вычисляем собственные значения
out.write('lambda:\n {}\n'.format(Lambda))

l = max(Lambda)  # максимальное собственное
out.write('l1:\n {}\n'.format(l))

b = ones(n)
for i in range(1, n):  # находим коэффиценты b
    b[i] = b[i - 1] * l - p[i - 1]
out.write('b:\n {}\n'.format(b))

x = sum([b[i] * C[n - i - 1] for i in range(n)], axis=0)  # вычисляем собственный вектор x
out.write('x:\n {}\n'.format(x))
out.write('x - norm:\n {}\n'.format(x / max(x)))

r = dot(a, x) - l * x  # находим вектор невязки
out.write('r:\n {}\n'.format(r))
out.write('||r||:\n {}\n'.format(norm(r, 1)))
