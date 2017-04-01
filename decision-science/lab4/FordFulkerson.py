#!/usr/bin/env python


class Edge:
    def __init__(self, start, finish, cost):
        self.start = start
        self.finish = finish
        self.cost = cost

    def __repr__(self):
        return '({})-{}->({})'.format(self.start, self.cost, self.finish)


class FlowNetwork:
    def __init__(self):
        self.adj = {}
        self.flow = {}

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

    def print_flow(self):
        for key in self.flow:
            print '{} - [{}]'.format(key, self.flow[key])

    def find_way(self, _from, _to, path):
        if _from == _to:
            return path

        for edge in self.get_edges(_from):
            residual = edge.cost - self.flow[edge]

            if residual > 0 and not (edge, residual) in path:
                result = self.find_way(edge.finish, _to, path + [(edge, residual)])

                if result is not None:
                    return result

    def max_flow(self, _from, _to):
        path = self.find_way(_from, _to, [])

        print 'path after enter MaxFlow: {}'.format(path)
        self.print_flow()
        print '-'*20

        while path is not None:
            flow = min(res for (edge, res) in path)
            for (edge, res) in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            self.print_flow()
            path = self.find_way(_from, _to, [])
            print 'path inside of while loop: {}'.format(path)
        self.print_flow()
        return sum(self.flow[edge] for edge in self.get_edges(_from))
