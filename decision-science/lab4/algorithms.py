#!/usr/bin/env python
from graphviz import Digraph


class Edge:
    def __init__(self, start, finish, cost):
        self.start = start
        self.finish = finish
        self.cost = cost

    def __repr__(self):
        return '({})-{}->({})'.format(self.start, self.cost, self.finish)


class FlowNetwork:
    def __init__(self, file_name):
        self.adj = {}
        self.flow = {}
        self.file_name = file_name

    def get_vertex(self):
        return self.adj.keys()

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError('u == v')

        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        edge.redge = redge
        redge.redge = edge

        self.adj[u].append(edge)
        self.adj[v].append(redge)

        self.flow[edge] = 0
        self.flow[redge] = 0

    def print_flow(self, out, keys):
        out.write('```\n')
        for key in keys:
            out.write('\t{0} - [{1}]\n'.format(key, self.flow[key]))
        out.write('```\n\n')

    def draw(self, file_name):
        g = Digraph('G', filename='{}.gv'.format(file_name), directory='out', format='png')
        for v in self.get_vertex():
            for e in self.get_edges(v):
                if e.cost != 0:
                    flow = '[{}]'.format(self.flow[e]) if self.flow[e] != 0 else ''
                    g.edge(e.start, e.finish, label=flow)
        g.view()

    def format_path(self, path):
        i = 0
        s = ''
        for (e, r) in path:
            start = '({})-'.format(e.start) if i == 0 else '-'
            s += ('{0}[{1}, {2}]->({3})'.format(start, e.cost, r, e.finish))
            i += 1
        return s

    def find_way(self, _from, _to, path):
        if _from == _to:
            return path

        for edge in self.get_edges(_from):
            residual = edge.cost - self.flow[edge]

            if residual > 0 and not (edge, residual) in path:
                result = self.find_way(edge.finish, _to, path + [(edge, residual)])

                if result is not None:
                    return result

    def bfs(self, _from, _to, _):
        visited = dict.fromkeys(self.adj.keys(), False)
        parent = dict.fromkeys(self.adj.keys())
        queue = [_from]
        visited[_from] = True

        while queue:
            u = queue.pop(0)
            for edge in self.get_edges(u):
                residual = edge.cost - self.flow[edge]
                if not visited[edge.finish] and residual > 0:
                    queue.append(edge.finish)
                    visited[edge.finish] = True
                    parent[edge.finish] = edge

        i = _to
        path = []
        while parent[i]:
            edge = parent[i]
            i = edge.start
            path.insert(0, (edge, edge.cost - self.flow[edge]))

        return path if visited[_to] else None

    def max_flow(self, _from, _to, find_func):
        out = file(self.file_name, 'w')
        path = find_func(_from, _to, [])

        while path is not None:
            flow = min(res for (edge, res) in path)
            out.write('* find path: `{0}`, with min res = {1}, change flow:\n'
                      .format(self.format_path(path), flow))
            edges = []
            for (edge, res) in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
                edges.append(edge)
            self.print_flow(out, edges)
            path = find_func(_from, _to, [])
        out.write('* maximal flow:\n')
        self.print_flow(out, self.flow)
        return sum(self.flow[edge] for edge in self.get_edges(_from))

    def ford_fulkerson(self, _from, _to):
        return self.max_flow(_from, _to, self.find_way)

    def edmonds_karp(self, _from, _to):
        return self.max_flow(_from, _to, self.bfs)
