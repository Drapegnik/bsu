#!/usr/bin/env python
from FordFulkerson import FlowNetwork

inp = file('task1.in', 'r')

if __name__ == '__main__':
    g = FlowNetwork()
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, w = inp.readline().split()
        g.add_edge(x, y, int(w))
    print g.max_flow('s', 't')
