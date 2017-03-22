def dijkstra(graph, start):
    """
    find min distance for all nodes from s
    :param graph: adjacency list of Edge objects
    :param start: start node
    :return:
        prev - list of previous node in min way
        dist - list of min distances
        debug_table - table with node state on each iteration
    """
    n = len(graph)
    prev = [-1]*n
    dist = [float('inf')]*n
    debug_table = [['(inf,{})'.format(start + 1)] for _ in range(n)]
    dist[start] = 0
    debug_table[start].append('({},{})'.format(0, start + 1))
    visited = [False]*n

    for i in range(n):
        u = -1
        for j in range(n):
            if not visited[j] and (u == -1 or dist[u] > dist[j]):
                u = j

        if dist[u] == float('inf'):
            break

        visited[u] = True
        debug_table[u][-1] += '*'

        for e in graph[u]:
            v = e.finish
            d = dist[u] + e.cost

            if dist[v] > d:
                dist[v] = d
                prev[v] = u
                debug_table[v].append('({}, {})'.format(d, u + 1))

    return dist, prev, debug_table


def floyd():
    pass
