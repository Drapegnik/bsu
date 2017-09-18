#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from algorithms import FlowNetwork


def build_graph(c, s, t, file_name):
    g = FlowNetwork(file_name)
    g.add_vertex('s')
    g.add_vertex('t')

    for next_s, i in s:
        g.add_vertex(next_s)
        g.add_edge('s', next_s, 1)

    for next_t, i in t:
        g.add_vertex(next_t)
        g.add_edge(next_t, 't', 1)

    for i, row in enumerate(c):
        for j, el in enumerate(row):
            if el == 0:
                g.add_edge('s{}'.format(i), 't{}'.format(j), 1)
    return g


def simplify_matrix(m):
    m = np.array([map(lambda x: x - min(m[i]), m[i]) for i in range(len(m))])
    for j in range(len(m)):
        m[:, j] = map(lambda x: x - min(m[:, j]), m[:, j])
    return m

if __name__ == '__main__':
    out = file('report.md', 'w')
    out.write(
        '# lab4\nPazhitnykh Ivan\n\n## task1\n* Find maximum flow in graph:'
        '\n![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491579189/ds-lab4-task1.png)\n')

    # task1
    inp = file('in/task1.in', 'r')
    g = FlowNetwork('task1')
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, w = inp.readline().split()
        g.add_edge(x, y, int(w))
    inp.close()
    print 'task1 max flow = {}'.format(g.max_flow('s', 't', out)[0])
    g.draw()

    out.write(
        '![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task1.gv.png)\n## task2\n'
        '* Find maximum flow in graph:\n![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1491579189/ds-lab4-task2.png)\n')

    # task2
    inp = file('in/task2.in', 'r')
    g = FlowNetwork('task2')
    map(g.add_vertex, inp.readline().split())
    m = int(inp.readline())
    for _ in range(m):
        x, y, min_w, w, f = inp.readline().split()
        g.add_edge(x, y, int(w), int(min_w), int(f))
    inp.close()
    g.draw(postfix='-1')
    out.write('* initial flow:\n')
    g.print_flow(out)
    out.write('![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task2-1.gv.png)\n')
    print 'task2 max flow = {}'.format(g.max_flow('s', 't', out)[0])
    g.draw(postfix='-2')
    out.write('![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab4/out/task2-2.gv.png)\n')
    out.write('## task3\n* Solve Assignment problem with coast matrix:\n')

    # task3
    inp = file('in/task3.in', 'r')
    n = int(inp.readline())
    s, t, c_in, flows = [], [], [], []
    flow = None

    for i in range(n):
        next_s = 's{}'.format(i)
        next_t = 't{}'.format(i)
        s.append((next_s, i))
        t.append((next_t, i))

    for i, line in enumerate(inp):
        row = map(lambda x: int(x), line.split())
        c_in.append(row)
    inp.close()
    out.write('```\n{}\n```\n'.format(np.array(c_in)))

    c = simplify_matrix(c_in)
    out.write('* simplified matrix:\n')
    out.write('```\n{}\n```\n'.format(c))

    k = 1
    g = build_graph(c, s, t, file_name='task3-{}'.format(k))
    out.write('* table with marks on last iterations of Ford-Fulkerson:\n\n')
    g.print_table_head(out)
    c_histtory = [np.copy(c)]

    while True:
        flow, marks = g.max_flow('s', 't', write=False)
        flows.append(flow)
        print 'task3: iteration{0}: max flow = {1}'.format(k, flow)
        g.print_table_row(out, marks)
        g.draw()

        if flow == n:
            break

        ss = filter(lambda (v, ind): marks[v], s)
        tt = filter(lambda (v, ind): not marks[v], t)
        not_tt = filter(lambda (v, ind): marks[v], t)
        min_c = min([c[i][j] for _, i in ss for _, j in tt])

        for _, i in ss:
            c[i] = map(lambda x: x - min_c, c[i])

        for _, j in not_tt:
            c[:, j] = map(lambda x: x + min_c, c[:, j])

        c_histtory.append(np.copy(c))
        k += 1
        g = build_graph(c, s, t, file_name='task3-{}'.format(k))

    for ind, c in enumerate(c_histtory):
        out.write('\n* iteration {0}, flow={1}:\n'.format(ind + 1, flows[ind]))
        out.write('```\n{}\n```\n'.format(c))
        out.write('![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/'
                  'lab4/out/task3-{}.gv.png)'.format(ind + 1))

    out.write('\n* cost value:\n')
    sum = 0
    expression = ''
    out.write('```\n')
    for v, ind in s:
        for e in g.get_edges(v):
            if g.flow[e]:
                out.write('{}\n'.format(e))
                i = ind
                j = int(e.finish[-1])
                expression = '{} + {}'.format(expression, c_in[i][j])
                sum += c_in[i][j]
    out.write('\n```\n')
    out.write('`C = {0} = {1}`'.format(expression[2:], sum))
