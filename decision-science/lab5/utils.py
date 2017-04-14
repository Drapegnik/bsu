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
