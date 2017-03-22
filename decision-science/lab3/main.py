import sys

from utils import *

inp = file('graph1.in', 'r')

MAX = 10 ** 10

n, m = map(lambda x: int(x), inp.readline().split())
g = [[] for _ in range(n)]

for i in range(m):
    x, y, d = map(lambda a: int(a), inp.readline().split())
    g[x - 1].append(Edge(x - 1, y - 1, d))

dist, prev = dijkstra(g, 0)

node = 0
while node != -1:
    try:
        node = int(raw_input('Please enter node number in [1, {}], or -1 for exit: '.format(n)))
        if node < 1 or node > n:
            raise ValueError
        node -= 1
    except ValueError:
        sys.stderr.write('Error, enter a number in [1, {}]!\n'.format(n))
        node = 0
        continue

    v = node
    way = []
    while v != -1:
        way.append(v)
        v = prev[v]

    s = '{}: '.format(dist[node])
    for v in reversed(way):
        s += '({})->'.format(v + 1)
    print s[:-2]
