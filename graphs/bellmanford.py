def bellman_ford(graph, vertices, start):
    """
    Bellman-Ford algorithm for shortest paths.
    Returns distance dictionary from 'start' to all nodes.
    """
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains a negative-weight cycle")
            return None

    return distances

if __name__ == "__main__":
    edges = [
        ('A', 'B', -1),
        ('A', 'C', 4),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 2),
        ('D', 'B', 1),
        ('D', 'C', 5),
        ('E', 'D', -3)
    ]
    vertices = {'A', 'B', 'C', 'D', 'E'}
    print("Shortest distances from A:", bellman_ford(edges, vertices, 'A'))
