import math
import numpy as np


def f(x):
    return float(x * (3 ** x + 1) ** (-1))


def cheb_nodes(a, b, n):
    return np.array(
        [(a + b) / 2.0 + (b - a) / 2.0 * math.cos((2 * i + 1) / (2.0 * n + 2.0) * math.pi)
         for i in range(n + 1)], dtype='float')


def diff_table(x, n, func):
    table = np.zeros((n, n), dtype='float')

    points = map(func, x)

    for i in range(n):
        table[i][0] = points[i]

    for i in range(1, n):
        for j in range(n - i):
            table[j][i] = (table[j + 1][i - 1] - table[j][i - 1]) / (x[j + i] - x[j])

    return table


def solve_newton(x, n, nodes, f):
    ans = 0.0
    for i in range(n):
        summ = f[i]
        for j in range(i):
            summ *= (x - nodes[j])
        ans += summ
    return ans


def printer_diff_tex_format(out, nodes, n, table):
    out.write('for $ m = ' + str(n) + '\Rightarrow n = ' + str(n - 1) + ' $.\n')
    out.write('\\begin{tabular}{')
    for i in range(n + 2):
        out.write('|c')
    out.write('|}\n\\hline\n')
    for i in range(n):
        out.write('{0:.4g} &'.format(nodes[i]))
        for j in range(n - 1):
            if j < n - i:
                out.write('{0:.4g} &'.format(table[i][j]))
            else:
                out.write(' &')
        if i == 0:
            out.write('{0:.4g}\\\\\\hline \n'.format(table[i][n - 1]))
        else:
            out.write('\\\\\\hline \n')
    out.write('\\end{tabular}\n')
    out.write('\n')


def print__err_tex_format(out, n, table):
    out.write('\\begin{center}')
    out.write('\\begin{tabular}{')
    for i in range(4):
        out.write('|c')
    out.write('|}\n\\hline\n')
    out.write('x &f(x) &P(x) &r(x)\\\\\\hline \n')
    for i in range(3 * n):
        for j in range(4):
            out.write('{0:.4g} '.format(table[i][j]))
            if (j != 3):
                out.write('&')
        out.write('\\\\\\hline \n')
    out.write('\\end{tabular}\n')
    out.write('\\end{center}')
    out.write('\n\n------------------------------------------------------------------\n\n')


A = -2.0
B = 2.0

out = open('output.txt', 'w')

for m in [3, 4, 5, 6, 8, 10]:
    x_n = cheb_nodes(A, B, m - 1)
    table = diff_table(x_n, m, f)
    printer_diff_tex_format(open('output.txt', 'a'), x_n, m, table)

    h = 3 * m - 1
    step = (B - A) / h

    err_table = []

    for i in range(3 * m):
        point = A + i * step
        direct = f(point)
        appr = solve_newton(point, m - 1, x_n, table[0])
        err = math.fabs(direct - appr)

        err_table.append([point, direct, appr, err])

    print__err_tex_format(open('output.txt', 'a'), m, err_table)
