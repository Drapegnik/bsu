from graphviz import Digraph


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


def draw_graph_with_path(m, path):
    """
        Render graph to png and save to filesystem
        :param m: flag to open image in new window
        :param path: Hamilton cycle for TSP
        :return: None
    """
    g = Digraph('G', filename='lab5.gv', directory='out', format='png')
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != float('inf'):
                kwargs = {'label': '{}'.format(int(m[i][j]))}
                if [i, j] in path:
                    kwargs = {
                        'color': 'red',
                        'label': '[{}]'.format(int(m[i][j])),
                        'penwidth': '3',
                        'fontsize': '20',
                        'fontcolor': 'red'
                    }
                g.edge('{}'.format(i + 1), '{}'.format(j + 1), **kwargs)
    g.render()
