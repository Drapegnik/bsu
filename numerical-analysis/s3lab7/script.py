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
f = a

out.write('A:\n {}\n'.format(a))

s = identity(n)

for i in range(n - 1):
    m = identity(n)
    m[n - 2 - i][:] = f[n - 1 - i][:]  # выделяем M^(-1)
    f = dot(m, f)  # умножаем A на M^(-1) слева
    f = dot(f, inv(m))  # умножаем A на M справа
    s = dot(s, inv(m))  # находим S

out.write('F:\n {}\n'.format(f))
out.write('S:\n {}\n'.format(s))

p = f[0][:]  # выделяем p
out.write('p:\n {}\n'.format(p))

x = Symbol('x')
Lambda = solve(x ** 5 - p[0] * x ** 4 - p[1] * x ** 3 - p[2] * x ** 2 - p[3] * x - p[4],
               x)  # вычисляем собственные значения
out.write('lambda:\n {}\n'.format(Lambda))

l = max(Lambda, )  # максимальное собственное
out.write('l1:\n {}\n'.format(l))

y = [l ** i for i in range(n - 1, -1, -1)]  # строим y
out.write('y1:\n {}\n'.format(y))

x = dot(s, y)  # находим собственный вектор
out.write('x1:\n {}\n'.format(x))

r = dot(a, x) - l * x  # находим вектор невязки
out.write('r:\n {}\n'.format(r))
out.write('||r||:\n {}\n'.format(norm(r, 1)))
# out.write('||p||:\n {}\n'.format(norm(p, 1)))

p = p.tolist()
p.insert(0, -1)
r1 = sum(-(l ** (n - i)) * p[i] for i in range(n + 1))  # считаем невязку собственного многочлена
out.write('r1:\n {}\n'.format(r1))

# out.write("{")
# for i in range(n):
#     out.write("{")
#     for j in range(n):
#         out.write("%.3f" % a[i][j])
#         if j != n-1:
#             out.write(",")
#     out.write("}")
#     if i != n-1:
#             out.write(",")
# out.write("}\n")
