def topological_sort(graph):
    """
    Topological Sort implementation using DFS.
    Returns list of nodes in topological order.
    """
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]

if __name__ == "__main__":
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
        'G': [],
        'H': []
    }
    print("Topological order:", topological_sort(graph))
