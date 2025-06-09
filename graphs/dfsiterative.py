def dfs_iterative(graph, start):
    """
    Depth-First Search (DFS - Iterative) implementation.
    Prints nodes in DFS order.
    """
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }
    print("DFS (Iterative) starting from A:")
    dfs_iterative(graph, 'A')
