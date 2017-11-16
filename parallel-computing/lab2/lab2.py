from math import ceil

from mpi4py import MPI

MODULE = 1000

A, b, rows, RESP_A = [], [], [], []
comm = MPI.COMM_WORLD
master = 0

N = 5  # FIXME
q2 = comm.size - 1
r3 = 2  # j
r2 = ceil((N - 1) / q2)
q3 = ceil((N - 1) / r3) + 1  # ???


def encode(i, j):
    return i * MODULE + j


def decode(x):
    return x // MODULE, x % MODULE,


def str_to_row(s):
    return [int(x) for x in s.split()][:-1]


def get_tile_size(k, i, j, r_i, r_j, n):
    i_s = k + i * r_i + 1
    i_e = min(k + (i + 1) * r_i + 1, n)  # n-1 ??
    j_s = j * r_j
    j_e = min((j + 1) * r_j, n)  # n-1 ??
    return i_s, i_e, j_s, j_e


def Tile():
    pass


def eliminate(a, args, ak, i, j):
    # FIXME PROBLEM UNDER THAT LINE
    return a[i][j] - args[i] * ak[j]


inp = open('input.txt', 'r')

if comm.rank == master:
    for line in inp:
        row = str_to_row(line)
        A.append(row)
        RESP_A.append([0] * len(row))
        b.append(int(line.split()[-1]))

    for k in range(N - 1):
        for i_gl in range(q2):
            for j_gl in range(q3):
                data = dict()
                proc_num = i_gl + 1
                i_start, i_end, j_start, j_end = get_tile_size(k, i_gl, j_gl, r_i=r2, r_j=r3, n=N)
                matrix = [row[j_start:j_end] for row in A[i_start:i_end]]
                arguments = [1.0 * A[i][k] / A[k][k] for i in range(i_start, i_end)]

                data['matrix'] = matrix
                data['args'] = arguments
                data['b'] = b[i_start:i_end]
                # data['A'] = A[k] ??
                comm.bcast(A[k], root=master)
                comm.send(data, dest=proc_num)

                response = comm.recv(source=proc_num)
                for r_i in range(i_start, i_end):
                    RESP_A[r_i][j_start:j_end] = matrix[i_start - r_i]
else:
    for i_gl in range(N - 1):
        for j_gl in range(q3):
            # k_line = comm.recv(source=master, tag=ROW_K) ??
            k_line = comm.bcast(None, root=master)
            data = comm.recv(source=master)
            # print(comm.rank, data)
            # FIXME PROBLEM UNDER THAT LINE
            response = [
                eliminate(data['matrix'], data['args'], k_line, i, j)
                for i in range(i_gl)
                for j in range(j_gl)
            ]
            comm.send(response, dest=master)
