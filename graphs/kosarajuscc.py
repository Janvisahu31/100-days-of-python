def kosaraju_scc(graph):
    """
    Kosaraju's Algorithm for finding SCCs.
    Returns list of SCCs.
    """
    def dfs(v, visited, stack):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse_graph(graph):
        reversed_g = {v: [] for v in graph}
        for u in graph:
            for v in graph[u]:
                reversed_g[v].append(u)
        return reversed_g

    def dfs_reverse(v, visited, component, reversed_g):
        visited.add(v)
        component.append(v)
        for neighbor in reversed_g[v]:
            if neighbor not in visited:
                dfs_reverse(neighbor, visited, component, reversed_g)

    stack = []
    visited = set()

    for v in graph:
        if v not in visited:
            dfs(v, visited, stack)

    reversed_g = reverse_graph(graph)
    visited.clear()
    sccs = []

    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            dfs_reverse(v, visited, component, reversed_g)
            sccs.append(component)

    return sccs

if __name__ == "__main__":
    graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [5],
        5: [3]
    }
    print("SCCs:", kosaraju_scc(graph))
