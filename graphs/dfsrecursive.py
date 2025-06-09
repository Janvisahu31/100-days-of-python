def dfs_recursive(graph, vertex, visited=None):
    """
    Depth-First Search (DFS - Recursive) implementation.
    Prints nodes in DFS order.
    """
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print("DFS starting from A:")
    dfs_recursive(graph, 'A')
