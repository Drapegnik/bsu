from math import ceil

from mpi4py import MPI

ROW_K = 1
MATRIX = 2
COL_B = 3
ARG = 4
MODULE = 1000

A, b, rows = [], [], []
comm = MPI.COMM_WORLD
master = 0

N = 5  # FIXME
q2 = comm.size - 1
r3 = 2  # j
r2 = ceil((N - 1) / q2)
q3 = ceil((N - 1) / r3)


def encode(i, j):
    return i * MODULE + j


def decode(x):
    return x // MODULE, x % MODULE,


def str_to_row(s):
    return [int(x) for x in s.split()][:-1]


def get_tile_size(k, i, j, r2, n):
    i_s = k + i * r2 + 1
    i_e = min(k + (i + 1) * r2 + 1, n)
    j_s = j * r2
    j_e = min((j + 1) * r2, n)
    return i_s, i_e, j_s, j_e


def Tile():
    pass


inp = open('input.txt', 'r')

if comm.rank == master:
    for line in inp:
        A.append(str_to_row(line))
        b.append(int(line.split()[-1]))

    for k in range(N - 1):
        for i_gl in range(q2):
            for j_gl in range(q3):
                data = dict()
                proc_num = i_gl + 1
                i_start, i_end, j_start, j_end = get_tile_size(k, i_gl, j_gl, r2, N)
                matrix = [row[j_start:j_end] for row in A[i_start:i_end]]
                arguments = [1.0 * A[i][k] / A[k][k] for i in range(i_start, i_end)]

                data['matrix'] = matrix
                data['args'] = arguments
                data['b'] = b[i_start:i_end]
                # data['A'] = A[k] ??
                comm.bcast(A[k], root=master)
                comm.send(data, dest=proc_num, tag=0)  # tag?
else:
    for k in range(N - 1):
        for i_gl in range(q2):
            for j_gl in range(q3):
                # k_line = comm.recv(source=master, tag=ROW_K) ??
                k_line = comm.bcast(None, root=master)
                data = comm.recv(source=master, tag=0)  # tag?
                print(comm.rank, data)
