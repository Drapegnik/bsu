import sys

from algorithms import dijkstra
from utils import *


def user_interaction(prev, dist, g_mat):
    while True:
        try:
            node = int(raw_input('Please enter node number in [1, {}], or 0 for exit: '.format(len(dist))))
            if node == 0:
                return
            if node < 1 or node > len(dist):
                raise ValueError
            node -= 1
        except ValueError:
            sys.stderr.write('Error, enter a number in [1, {}]!\n'.format(len(dist)))
            continue

        v = node
        way = []
        while v != -1:
            way.append(v)
            v = prev[v]

        last = way[-1]
        s = '{}: ({})'.format(dist[node], last + 1)
        for v in reversed(way[:-1]):
            s += '-{}->({})'.format(int(g_mat[last][v]), v + 1)
            last = v
        print s


print '-'*35 + '\ntask1 - shortest ways from (1)\n' + '-'*35
g_list, g_mat = read_graph_list('task1.in')
dist, prev, table = dijkstra(g_list, 0)
user_interaction(prev, dist, g_mat)
write_debug_table('task2.out.md', table)

print '\n' + '-'*35 + '\ntask2\n' + '-'*35
g_mat = read_graph_matrix('task2.in')
