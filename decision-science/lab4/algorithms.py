#!/usr/bin/env python
from graphviz import Digraph


class Edge:
    def __init__(self, start, finish, weight=0):
        self.start = start
        self.finish = finish
        self.weight = weight

    def __repr__(self):
        return '({0})-{1}->({2})'.format(self.start, self.weight, self.finish)


class Mark:
    def __init__(self, parent=None, flow=float('inf'), edge=None):
        self.parent = parent
        self.flow = flow
        self.edge = edge

    def __repr__(self):
        return '({}, {})'.format(self.parent, self.flow)


class FlowNetwork:
    def __init__(self, file_name):
        self.adj = {}
        self.flow = {}
        self.file_name = file_name

    def get_vertex(self):
        vertex = self.adj.keys()
        vertex.sort()
        return vertex

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError('u == v')

        edge = Edge(u, v, w)
        redge = Edge(v, u)
        edge.redge = redge
        redge.redge = edge

        self.adj[u].append(edge)
        self.adj[v].append(redge)

        self.flow[edge] = 0
        self.flow[redge] = 0

    def ford_fulkerson(self, _from, _to):
        return self.max_flow(_from, _to, self.get_marks)

    def edmonds_karp(self, _from, _to):
        return self.max_flow(_from, _to, self.bfs)

    def get_marks(self, _from, _to):
        marks = dict.fromkeys(self.get_vertex())
        marks[_from] = Mark()
        queue = [_from]

        while queue:
            v = queue.pop(0)
            if v == _to:
                return marks

            for edge in self.get_edges(v):
                if not marks[edge.finish] and self.flow[edge] < edge.weight:
                    flow = min(abs(marks[v].flow), edge.weight - self.flow[edge])
                    marks[edge.finish] = Mark(v, flow, edge)
                    queue.append(edge.finish)

            for edge in self.get_edges(v):
                if not marks[edge.finish] and self.flow[edge.redge] > 0:
                    flow = min(abs(marks[v].flow), self.flow[edge.redge])
                    marks[edge.finish] = Mark(v, -flow, edge.redge)
                    queue.append(edge.finish)

    def bfs(self, _from, _to):
        visited = dict.fromkeys(self.get_vertex(), False)
        marks = dict.fromkeys(self.get_vertex())
        queue = [_from]
        visited[_from] = True
        marks[_from] = Mark()
        min_flow = marks[_from].flow

        while queue:
            v = queue.pop(0)
            for edge in self.get_edges(v):
                flow = edge.weight - self.flow[edge]
                if not visited[edge.finish] and flow > 0:
                    queue.append(edge.finish)
                    visited[edge.finish] = True
                    marks[edge.finish] = Mark(v, flow, edge)
                    min_flow = min(min_flow, flow)

        for v in marks:
            if marks[v]:
                marks[v].flow = min_flow

        return marks if visited[_to] else None

    def max_flow(self, _from, _to, find_func):
        out = file(self.file_name + '.md', 'w')
        self.print_table_head(out)
        marks = find_func(_from, _to)

        while marks is not None:
            self.print_table_row(out, marks)
            i = _to
            while marks[i] is not None:
                if marks[i].parent is None:
                    break
                self.flow[marks[i].edge] += marks[i].flow
                i = marks[i].parent
            marks = find_func(_from, _to)

        flow = sum(self.flow[edge] for edge in self.get_edges(_from))
        out.write('\n* maximal flow = {}:\n'.format(flow))
        self.print_flow(out)
        return flow

    def print_flow(self, out):
        out.write('```\n')
        keys = self.flow.keys()
        keys.sort()
        for key in keys:
            out.write('\t{0} - [{1}]\n'.format(key, self.flow[key]))
        out.write('```\n\n')

    def print_table_head(self, out):
        out.write('* table with marks by iteration:\n\n')
        out.write(reduce(lambda s, x: '{0} | {1} '.format(s, x), self.get_vertex()) + '\n')
        out.write('--- | '*len(self.get_vertex()) + '\n')

    def print_table_row(self, out, marks):
        for v in self.get_vertex():
            out.write('`{}` | '.format(marks[v]))
        out.write('\n')

    def draw(self):
        g = Digraph('G', filename='{}.gv'.format(self.file_name), format='png')
        for v in self.get_vertex():
            for e in self.get_edges(v):
                if e.weight != 0:
                    flow = '[{0}/{1}]'.format(self.flow[e], e.weight) if self.flow[e] != 0 else ''
                    g.edge(e.start, e.finish, label=flow)
        g.render()
