import numpy as np


class Edge:
    def __init__(self, start, finish, cost):
        self.start = start
        self.finish = finish
        self.cost = cost


def read_graph_list(file_name):
    """
    Read graph list from file and return adjacency list and matrix
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

    return g_list, g_mat.tolist()


def read_graph_matrix(file_name):
    """
    Read graph matrix from file
    :param file_name: name of file with graph info
    :return: matrix - adjacency matrix: g_matrix[v1][v2]==v1_v2_cost
    """
    inp = file(file_name, 'r')
    n = int(inp.readline())
    matrix = []
    for i in range(n):
        matrix.append(map(lambda x: float(x), inp.readline().split()))
    return matrix
