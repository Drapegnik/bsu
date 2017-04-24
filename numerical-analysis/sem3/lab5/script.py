# coding=utf-8
from numpy import *
from numpy.linalg import *

inp = open('input.txt', 'r')
out = open('output.txt', 'w')

n, m = 5, 5
A, f, E = [], [], identity(n)
eps = 10 ** (-5)

for line in inp:  # читаем А и b
    temp = [float(x) for x in line.split()]
    f.append(temp.pop())
    A.append(temp)

a, b = array(A), array(f).transpose()

out.write('A:\n {}\n'.format(a))
out.write('b:\n {}\n'.format(b))

D = diag(a)  # диагональные ел-ты A
# LD = inv(tril(a))  # получаем обратную нижнего треугольника с диагональю
# U = triu(a) - E * D  # нижний треугольник
xk, x = array(b / D), zeros(n)  # начальное приближение
k = 0

out.write('x0:\n {}\n'.format(xk))
out.write('D:\n {}\n'.format(D))
# out.write('(L+D)^(-1):\n {}\n'.format(LD))
# out.write('U:\n {}\n'.format(U))

while True:  # итерационный процесс
    # x = -dot(dot(LD, U), xk) + dot(LD, b)
    for i in range(n):
        x[i] = b[i] / a[i][i] - sum([x[j] * a[i][j] / a[i][i] for j in range(i)]) - sum(
            [xk[j] * a[i][j] / a[i][i] for j in range(i + 1, n)])

    if abs(norm(xk, 1) - norm(x, 1)) < eps:
        break
    xk = array(x)
    k += 1

out.write('x:\n {}\n'.format(x))
out.write('k:\n {}\n'.format(k))

r = dot(A, x) - f  # находим вектор невязки

out.write('r:\n {}\n'.format(r))
out.write('||r||:\n {}\n'.format(norm(r, 1)))
# out.write('|| (L+D)^(-1)*U ||:\n {}\n'.format(norm(dot(LD, U), inf)))
out.write('eps:\n {}\n'.format(eps))
