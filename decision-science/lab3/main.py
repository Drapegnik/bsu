import sys

import numpy as np

from utils import *


def read_graph(file_name):
    """
    Read graph and return adjacency list and matrix
    :param file_name: name of file with graph info
    :return:
        g_list - adjacency list: g_list[0]==[Edge, Edge, ...]
        g_matrix - adjacency matrix: g_matrix[v1][v2]==v1_v2_cost
    """
    inp = file(file_name, 'r')
    n, m = map(lambda x: int(x), inp.readline().split())
    g_list = [[] for _ in range(n)]
    g_mat = np.zeros((n, n))
    g_mat.fill(float('inf'))

    for i in range(m):
        x, y, d = map(lambda a: int(a), inp.readline().split())
        x -= 1
        y -= 1

        g_list[x].append(Edge(x, y, d))
        g_mat[x][y] = d

    return g_list, g_mat


g_list, g_mat = read_graph('graph1.in')
dist, prev = dijkstra(g_list, 0)

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
    # 5: (1)->(4)->(2)->(6)->(5)->(9)->(7)->(10)
