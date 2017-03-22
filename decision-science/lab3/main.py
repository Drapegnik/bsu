import sys

from algorithms import dijkstra
from utils import *

g_list, g_mat = read_graph_list('graph1.in')
dist, prev = dijkstra(g_list, 0)
read_graph_matrix('graph2.in')

node = 0
while node != -1:
    try:
        node = int(raw_input('Please enter node number in [1, {}], or -1 for exit: '.format(len(dist))))
        if node < 1 or node > len(dist):
            raise ValueError
        node -= 1
    except ValueError:
        sys.stderr.write('Error, enter a number in [1, {}]!\n'.format(len(dist)))
        node = 0
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
