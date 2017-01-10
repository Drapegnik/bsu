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

# k = (log(eps) - log(sum([abs(el) ** 2 for el in absolute(a - tril(a))])))/log(0.5)

E, U = identity(n), identity(n)
k = 0
ak = a  # копия А

while (True):
    L = tril(ak)
    temp = absolute(ak - L)  # получаем верхний треугольник, без диагонали

    sigma = sum([abs(el) ** 2 for el in temp])  # считаем сумму квадратов недиагональных
    if (sigma <= eps):  # условие
        break
    i, j = unravel_index(temp.argmax(), temp.shape)  # индексы максимального

    alpha = math.atan(2 * ak[i][j] / (ak[i][i] - ak[j][j])) / 2  # считаем угол
    uk = identity(n)
    uk[i][i], uk[i][j], uk[j][j], uk[j][i] = cos(alpha), -sin(alpha), cos(alpha), sin(alpha)

    # tan2phi = 2 * ak[i][j] / (ak[i][i] - ak[j][j])
    # cos2phi = 1 / sqrt(1 + tan2phi ** 2)
    # cosphi = sqrt((1 + cos2phi) / 2)
    # sinphi = sign(ak[i][j] / (ak[i][i] - ak[j][j])) * sqrt((1 - cos2phi) / 2)
    #
    # uk = identity(n)
    # uk[i][i], uk[i][j], uk[j][j], uk[j][i] = cosphi, -sinphi, cosphi, sinphi

    ak = dot(dot(uk.transpose(), ak), uk)  # Ukt*A*Uk
    U = dot(U, uk)  # U*Uk
    k += 1

out.write('Ak:\n {}\n'.format(ak))

out.write('lambdа:\n {}\n'.format(ak.diagonal()))
out.write('U:\n {}\n'.format(U))
out.write('k:\n {}\n'.format(k))

lmax = max(ak.diagonal())  # max lambda
out.write('lmax:\n {}\n'.format(lmax))
x = U.transpose()[ak.diagonal().argmax()]  # получаем x
x /= max(x)  # нормируем
out.write('x:\n {}\n'.format(x))

r = dot(a, x) - lmax * x  # находим вектор невязки
out.write('r:\n {}\n'.format(r))
out.write('||r||:\n {}\n'.format(norm(r, 1)))

p = [4.58801522, -7.82119475, 6.11344651, -2.15665219, 0.2685558]  # из Данилевского
out.write('p:\n {}\n'.format(p))
p.insert(0, -1)
r1 = sum(-(lmax ** (n - i)) * p[i] for i in range(n + 1))  # считаем невязку собственного многочлена Pn(l)
out.write('Pn(l):\n {}\n'.format(r1))

out.write('eps:\n {}\n'.format(eps))
