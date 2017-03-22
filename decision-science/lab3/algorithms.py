def dijkstra(graph, s):
    """
    find min distance for all nodes from s
    :param graph: adjacency list of Edge objects
    :param s: start node
    :return:
        prev - list of previous node in min way
        dist - list of min distances
    """
    n = len(graph)
    prev = [-1]*n
    dist = [float('inf')]*n
    dist[s] = 0
    visited = [False]*n

    for i in range(n):
        u = -1
        for j in range(n):
            if not visited[j] and (u == -1 or dist[u] > dist[j]):
                u = j

        if dist[u] == float('inf'):
            break

        visited[u] = True

        for e in graph[u]:
            v = e.finish
            d = dist[u] + e.cost

            if dist[v] > d:
                dist[v] = d
                prev[v] = u

    return dist, prev
