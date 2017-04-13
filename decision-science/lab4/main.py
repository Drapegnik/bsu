#!/usr/bin/env python

from algorithms import FlowNetwork

if __name__ == '__main__':
    # task1
    inp = file('in/task1.in', 'r')
    g = FlowNetwork('out/task1')
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, w = inp.readline().split()
        g.add_edge(x, y, int(w))
    inp.close()
    print 'task1 max flow = {}'.format(g.ford_fulkerson('s', 't')[0])
    g.draw()

    # task2
    inp = file('in/task2.in', 'r')
    g = FlowNetwork('out/task2')
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, w = inp.readline().split()
        g.add_edge(x, y, float(w))
    inp.close()
    print 'task2 max flow = {}'.format(g.edmonds_karp('s', 't')[0])
    g.draw()
