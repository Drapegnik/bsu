#!/usr/bin/env python
from graphviz import Digraph


class Edge:
    def __init__(self, start, finish, weight=0, redge=False):
        self.start = start
        self.finish = finish
        self.weight = weight
        self.redge = redge  # flag for saying, that its incoming edge

    def __repr__(self):
        return '({0})-{1}->({2})'.format(self.start, self.weight, self.finish)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, another):
        return self.start == another.start and self.finish == another.finish and self.weight == another.weight


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

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_vertex(self):
        vertex = self.adj.keys()
        vertex.sort()
        return vertex

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError('u == v')

        edge = Edge(u, v, w)
        redge = Edge(u, v, w, redge=True)

        self.adj[u].append(edge)
        self.adj[v].append(redge)

        self.flow[edge] = 0

    def get_edges(self, v):
        """
        Return outcoming edges for v
        :param v: node
        :return: list of Edge object's
        """
        return filter(lambda e: not e.redge, self.adj[v])

    def get_redges(self, v):
        """
        Return incoming edges for v
        :param v: node
        :return: list of Edge object's
        """
        return filter(lambda e: e.redge, self.adj[v])

    def ford_fulkerson(self, _from, _to, write=True):
        """
        Wrapper on max_flow() method, with get_marks() as search function
        :param _from: a source
        :param _to: a sink
        :param write: param for disabling file outputs
        """
        return self.max_flow(_from, _to, self.get_marks, write)

    def edmonds_karp(self, _from, _to, write=True):
        """
        Wrapper on max_flow() method, with bfs() as search function
        :param _from: a source
        :param _to: a sink
        :param write: param for disabling file outputs
        """
        return self.max_flow(_from, _to, self.bfs, write)

    def get_marks(self, _from, _to):
        """
        Set marks for nodes
        :param _from: a source
        :param _to: a sink
        :return: list og Mark object's
        """
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

            for redge in self.get_redges(v):
                if not marks[redge.start] and self.flow[redge] > 0:
                    flow = min(abs(marks[v].flow), self.flow[redge])
                    marks[redge.start] = Mark(v, -flow, redge)
                    queue.append(redge.start)

        return marks

    def bfs(self, _from, _to):
        """
        Breadth-first search alghoritm implementation
        :param _from: a source
        :param _to: a sink
        :return: list of Mark object's
        """
        visited = dict.fromkeys(self.get_vertex(), False)
        marks = dict.fromkeys(self.get_vertex())
        queue = [_from]
        visited[_from] = True
        marks[_from] = Mark()

        while queue:
            v = queue.pop(0)
            for edge in self.get_edges(v):
                flow = edge.weight - self.flow[edge]
                if not visited[edge.finish] and flow > 0:
                    queue.append(edge.finish)
                    visited[edge.finish] = True
                    marks[edge.finish] = Mark(v, flow, edge)

        return self.find_min_flow(marks, _to)

    @staticmethod
    def find_min_flow(marks, _to):
        """
        Set min flow value during the min way from sink to source
        :param marks: list of Mark object's
        :param _to: a sink
        :return: list of Mark object's with new flow value
        """
        i = _to
        min_flow = float('inf')
        while marks[i] is not None:
            if marks[i].parent is None:
                break
            min_flow = min(min_flow, marks[i].flow)
            i = marks[i].parent

        i = _to
        while marks[i] is not None:
            if marks[i].parent is None:
                break
            marks[i].flow = min_flow
            i = marks[i].parent
        return marks

    def max_flow(self, _from, _to, find_func, write=True):
        """
        Find max flow in network
        :param _from: a source
        :param _to: a sink
        :param find_func search function implementation
        :param write: param for disabling file outputs
        :return: max flow, marks from last iteration
        """
        if write:
            out = file(self.file_name + '.md', 'w')
            out.write('* table with marks by iteration:\n\n')
            self.print_table_head(out)
        marks = find_func(_from, _to)

        while marks[_to] is not None:
            if write:
                self.print_table_row(out, marks)
            i = _to
            while marks[i] is not None:
                if marks[i].parent is None:
                    break
                self.flow[marks[i].edge] += marks[i].flow
                i = marks[i].parent
            marks = find_func(_from, _to)

        flow = sum(self.flow[edge] for edge in self.get_edges(_from))
        if write:
            self.print_table_row(out, marks)
            out.write('\n* maximal flow = {}:\n'.format(flow))
            self.print_flow(out)
            out.close()
        return flow, marks

    def print_flow(self, out):
        out.write('```\n')
        keys = self.flow.keys()
        keys.sort()
        for key in keys:
            out.write('\t{0} - [{1}]\n'.format(key, self.flow[key]))
        out.write('```\n\n')

    def print_table_head(self, out):
        out.write(reduce(lambda s, x: '{0} | {1} '.format(s, x), self.get_vertex()) + '\n')
        out.write('--- | '*len(self.get_vertex()) + '\n')

    def print_table_row(self, out, marks):
        for v in self.get_vertex():
            out.write('`{}` | '.format(marks[v]))
        out.write('\n')

    def draw(self, show=False):
        """
        Render graph to png and save to filesystem
        :param show: flag to open image in new window
        :return: None
        """
        g = Digraph('G', filename='{}.gv'.format(self.file_name), format='png')
        for v in self.get_vertex():
            for e in self.get_edges(v):
                flow = '[{0}/{1}]'.format(self.flow[e], e.weight) if self.flow[e] != 0 else ''
                g.edge(e.start, e.finish, label=flow)
        g.render(view=show)
