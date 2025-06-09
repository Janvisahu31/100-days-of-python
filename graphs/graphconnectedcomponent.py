def dfs(graph, vertex, visited):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def connected_components(graph):
    """
    Finds number of connected components in graph.
    """
    visited = set()
    count = 0

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited)
            count += 1

    return count

if __name__ == "__main__":
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
        4: []
    }
    print("Number of connected components:", connected_components(graph))
