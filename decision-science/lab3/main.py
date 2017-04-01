import os
import sys

from algorithms import dijkstra, floyd
from utils import *


def dialog(size):
    try:
        node = int(raw_input('Please enter node number in [1, {}], or -1 for exit: '.format(size)))
        if node == -1:
            return -1
        if node < 1 or node > size:
            raise ValueError
        node -= 1
    except ValueError:
        sys.stderr.write('Error, enter a number in [1, {}]!\n'.format(len(dist)))
        return False
    return node


def user_interaction(prev, dist, g_mat):
    while True:
        node = dialog(len(dist))

        if node == -1:
            return

        if node is False:
            continue

        v = node
        way = []
        while v != -1:
            way.append(v)
            v = prev[v]

        last = way[-1]
        s = 'd={}: ({})'.format(dist[node], last + 1)
        for v in reversed(way[:-1]):
            s += '-{}->({})'.format(int(g_mat[last][v]), v + 1)
            last = v
        print s


TASK1_START = 0
print '-'*35 + '\ntask1 - shortest ways from ({})\n'.format(TASK1_START + 1) + '-'*35
g_list, g_mat = read_graph_list('task1.in')
dist, prev, table = dijkstra(g_list, TASK1_START)
user_interaction(prev, dist, g_mat)
write_debug_table('task1.out.md', table)

print '\n' + '-'*35 + '\ntask2\n' + '-'*35
os.remove('task2.out.md')
g_mat = read_graph_matrix('task2.in')
dist, path = floyd(g_mat)
