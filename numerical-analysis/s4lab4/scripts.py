import numpy as np

n = 50
A = -2.0
B = 2.0
w = 1


def get_points():
    return [A + i * (B - A) / n for i in range(n + 1)]


def f(x):
    return float(x * (3 ** x + 1) ** (-1))


def phi_0(x):
    return 1


def phi_1(x):
    return x


def phi_2(x):
    return x ** 2


phi = [phi_0, phi_1, phi_2]


def dot_prod(f, g):
    return w * np.dot(map(f, get_points()), map(g, get_points()))


lhs = [[dot_prod(phi[k], phi[i]) for i in range(3)] for k in range(3)]
rhs = [dot_prod(f, phi[i]) for i in range(3)]
c = np.linalg.solve(lhs, rhs)


def p(x):
    return np.sum([c[i] * x ** i for i in range(3)])


def deviation():
    return (np.sum(map(lambda x: w * (f(x) - p(x)) ** 2, get_points()))/(n+1))**0.5


print map(lambda x: format(x, '.3g'), c)
print format(deviation(), '.5g')
