from math import ceil

import numpy as np
from mpi4py import MPI

A, rows = [], []
comm = MPI.COMM_WORLD
master = 0

N = 5  # rows
M = 6  # cols
q2 = comm.size - 1
r3 = 2  # j
r2 = ceil((N - 1) / q2)
q3 = int(ceil(M / r3) + 1)


def str_to_row(s):
    return [int(x) for x in s.split()]


def get_tile_size(k, i, j, r_i, r_j):
    i_s = k + i * r_i + 1
    i_e = min(k + (i + 1) * r_i + 1, N)
    j_s = j * r_j
    j_e = min((j + 1) * r_j, M)
    return i_s, i_e, j_s, j_e


def eliminate(a, args, ak, i, j):
    """
    Gauss–Jordan elimination
    """
    return a[i][j] - args[i] * ak[j]


inp = open('input.txt', 'r')

if comm.rank == master:
    for line in inp:
        row = str_to_row(line)
        A.append(np.array(row[:]))
    A = np.array(A)
    print('> input:\n{}\n'.format(A))

    for k in range(N - 1):
        r2 = ceil((N - 1 - k) / (comm.size - 1))
        # sending data to subprocess
        for i_gl in range(q2):
            for j_gl in range(q3):
                data = dict()
                proc_num = i_gl + 1
                i_start, i_end, j_start, j_end = get_tile_size(k, i_gl, j_gl, r_i=r2, r_j=r3)
                matrix = A[i_start:i_end, j_start:j_end]
                arguments = [1.0 * A[i][k] / A[k][k] for i in range(i_start, i_end)]

                data['matrix'] = matrix
                data['args'] = arguments
                data['ak'] = A[k][j_start:j_end]
                comm.send(data, dest=proc_num)

        # receive data
        for i_gl in range(q2):
            for j_gl in range(q3):
                proc_num = i_gl + 1
                i_start, i_end, j_start, j_end = get_tile_size(k, i_gl, j_gl, r_i=r2, r_j=r3)
                response = comm.recv(source=proc_num)

                if response:
                    A[i_start:i_end, j_start:j_end] = response
else:
    for i_gl in range(N - 1):
        for j_gl in range(q3):
            data = comm.recv(source=master)
            matrix = data['matrix']
            print(comm.rank, data)
            rows, cols = matrix.shape
            if not rows:
                comm.send(None, dest=master)

            # forward elimination
            response = [[
                eliminate(matrix, data['args'], data['ak'], i, j)
                for j in range(cols)
            ] for i in range(rows)]
            comm.send(response, dest=master)

if comm.rank == master:
    print('> forward elimination:\n{}\n'.format(A))
    # back substitution
    for i in reversed(range(1, N)):
        for i2 in reversed(range(i)):
            arg = A[i2][i] / A[i][i]
            A[i2][i] -= A[i][i] * arg
            A[i2][M - 1] -= A[i][i] * arg
    x = [A[i][M - 1] / A[i][i] for i in range(N)]
    print('> back substitution:\n{}\n'.format(A))
    print('> x={}'.format(x))
