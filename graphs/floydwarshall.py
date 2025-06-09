def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for All-Pairs Shortest Path.
    Returns distance matrix.
    """
    dist = [[float('inf')] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
        dist[i][i] = 0

    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

if __name__ == "__main__":
    graph = {
        0: {1: 5, 3: 10},
        1: {2: 3},
        2: {3: 1},
        3: {}
    }
    dist = floyd_warshall(graph)
    print("Shortest distance matrix:")
    for row in dist:
        print(row)
