# coding=utf-8
from numpy import *
from numpy.linalg import *
from math import *

inp = open('input.txt', 'r')
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
# At = a.transpose()  # находим Аt
b = array(f).transpose()

# a, b = dot(At, a), dot(At, b)  # перемножаем А на Аt, теперь А - симметрическая,то же самое с b

out.write('A:\n {}\n'.format(a))
out.write('b:\n {}\n'.format(b))

diagA = diag(a)  # диагональные ел-ты A
g = b / diagA  # находим g
B = array(a) - E * diagA  # находим B
for i in range(n):
    for j in range(m):
        B[i][j] /= (-diagA[i])

# t = 1 / norm(a, inf)  # вычисляем t 
# g = b * t  # находим g и B 
# B = array(E) - a * t

normB = norm(B, inf)
k = log(eps * (1 - normB) / norm(g, 1), normB) - 1

out.write('g:\n {}\n'.format(g))
out.write('B:\n {}\n'.format(B))
out.write('norma B:\n {}\n'.format(normB))
out.write('k teor:\n {}\n'.format(k))

xk, x = array(g), zeros(n)
k = 0

while True:  # итерационный процесс
    x = dot(B, xk) + g
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
