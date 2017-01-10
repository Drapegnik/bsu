import sys

import numpy as np
from mpi4py import MPI

from task import Point, Index, ProcSquare, Region
from utils import formatting, Timer, get_dimensions

comm = MPI.COMM_WORLD
master = 0
top, right = 1.0, 1.0
rows, cols = int(sys.argv[1]), int(sys.argv[2])
min_diff = float('inf')
epsilon = 10.0 ** (-7)

if comm.rank == master:
    t = Timer('TOTAL')
    t_init = Timer('initialization')
    print formatting(comm.rank, 'Calculate differential equation with {0} processes'.format(comm.size))

comm.bcast(rows, root=master)
comm.bcast(cols, root=master)

comm_rows, comm_cols = get_dimensions(rows, comm.size)

if comm.rank == master:
    print formatting(comm.rank, 'with {0}D topology: {1}x{2}'.format(
        2 if comm_cols > 1 else 1, comm_rows, comm_cols))

topo = comm.Create_cart(dims=[comm_rows, comm_cols], periods=[0, 0], reorder=True)
cart_comm = MPI.Cartcomm(topo)
coords = cart_comm.Get_coords(comm.rank)
comm_i, comm_j = coords

step_x = right / (cols - 1) if cols > 1 else float('inf')
step_y = -top / (rows - 1) if rows > 1 else float('inf')

first_cols = cols / comm_cols + cols % comm_cols
next_cols = cols / comm_cols
first_rows = rows / comm_rows + rows % comm_rows
next_rows = rows / comm_rows


def get_calc_reg(i, j):
    return {
        'rows': first_rows if i == 0 else next_rows,
        'rows_start': 0 if i == 0 else first_rows + (i - 1) * next_rows,
        'cols': first_cols if j == 0 else next_cols,
        'cols_start': 0 if j == 0 else first_cols + (j - 1) * next_cols,
    }


index = Index(**get_calc_reg(comm_i, comm_j))
point = Point(
    x=0.0 if index.cols_start == 0 else step_x * index.cols_start,
    y=top if index.rows_start == 0 else top + step_y * index.rows_start
)

region = Region(
    top=index.rows_start,
    right=index.cols_start + index.cols,
    bottom=index.rows_start + index.rows,
    left=index.cols_start
)

square = ProcSquare(
    full_region=Region(right=cols, bottom=rows),
    region=region,
    left_top=point,
    step_x=step_x,
    step_y=step_y
)

print formatting(comm.rank, '\n$\tcoord:\t{0}\n$\tregion:\t{1}\n$\tpoint:\t{2}'.format(coords, region, point))

cart_comm.barrier()
iterations = 0
if comm.rank == master:
    t_init.finish(comm.rank)
    t_calc = Timer('calculation')

while min_diff > epsilon:
    square.exch(cart_comm)
    square.calc()
    diff = square.diff
    iterations += 1
    min_diff = cart_comm.allreduce(diff, op=MPI.MAX)

if comm.rank == master:
    t_calc.finish(master)
    t_calc = Timer('collecting results')

    results = []
    for i in range(rows):
        results.append(np.zeros(cols))

    for i in range(index.rows):
        for j in range(index.cols):
            results[i][j] = square.get(i, j)

    for rank in range(1, comm.size):
        comm_i, comm_j = cart_comm.Get_coords(rank)
        index = Index(**get_calc_reg(comm_i, comm_j))
        res_i_j = comm.recv(source=rank)

        for row_i in range(index.rows):
            for col_j in range(index.cols):
                results[index.rows_start + row_i][index.cols_start + col_j] \
                    = res_i_j[row_i * index.cols + col_j]

    t_calc.finish(master)
    t.finish(master)

    if rows < 10 and cols < 10:
        print formatting(master, 'results:')

    out = open('output.txt', 'w')
    for row in results:
        str_row = ('{:2f}\t' * len(row)).format(*row)
        if rows < 10 and cols < 10:
            print '\t' + str_row
        out.write(str_row + '\n')

    print formatting(master, 'iterations: {}'.format(iterations))

else:
    comm.send(square.data(), dest=master)
