#!/usr/bin/env python
from graphviz import Digraph


class Edge:
    def __init__(self, start, finish, weight=0, min_weight=0, redge=False):
        self.start = start
        self.finish = finish
        self.min_weight = min_weight
        self.weight = weight
        self.redge = redge  # flag for saying, that its incoming edge

    def __repr__(self):
        return '({0})-{1}{2}->({3})'.format(
            self.start,
            '{},'.format(self.min_weight) if self.min_weight != 0 else '',
            self.weight, self.finish)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, another):
        return self.start == another.start \
               and self.finish == another.finish \
               and self.weight == another.weight \
               and self.min_weight == another.min_weight


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

    def add_edge(self, u, v, w=0, min_w=0, f=0):
        if u == v:
            raise ValueError('u == v')

        edge = Edge(u, v, w, min_w)
        redge = Edge(u, v, w, min_w, redge=True)

        self.adj[u].append(edge)
        self.adj[v].append(redge)

        self.flow[edge] = f

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
                if not marks[redge.start] and self.flow[redge] > redge.min_weight:
                    flow = min(abs(marks[v].flow), self.flow[redge] - redge.min_weight)
                    marks[redge.start] = Mark(v, -flow, redge)
                    queue.append(redge.start)

        return marks

    def max_flow(self, _from, _to, out=None, write=True):
        """
        Find max flow in network
        :param _from: a source
        :param _to: a sink
        :param write: param for disabling file outputs
        :return: max flow, marks from last iteration
        """
        if write:
            out.write('* table with marks by iteration:\n\n')
            self.print_table_head(out)
        marks = self.get_marks(_from, _to)

        while marks[_to]:
            if write:
                self.print_table_row(out, marks)
            i = _to
            while marks[i].parent:
                self.flow[marks[i].edge] += marks[i].flow
                i = marks[i].parent
            marks = self.get_marks(_from, _to)

        flow = sum(self.flow[edge] for edge in self.get_edges(_from))
        if write:
            self.print_table_row(out, marks)
            out.write('\n* maximal flow = {}:\n'.format(flow))
            self.print_flow(out)
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

    def draw(self, show=False, postfix=''):
        """
        Render graph to png and save to filesystem
        :param show: flag to open image in new window
        :return: None
        """
        g = Digraph('G', filename='{}.gv'.format(self.file_name + postfix), directory='out', format='png')
        for v in self.get_vertex():
            for e in self.get_edges(v):
                flow = ''
                if self.flow[e] != 0:
                    if self.flow[e] != e.weight:
                        flow = '[{0}/{1}]'.format(self.flow[e], e.weight)
                    else:
                        flow = '[{}]'.format(self.flow[e])
                color = 'red' if self.flow[e] != 0 else ''
                g.edge(e.start, e.finish, label=flow, color=color)
        g.render(view=show)