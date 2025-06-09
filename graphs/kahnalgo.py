from collections import deque

def topological_sort_kahn(graph):
    """
    Topological Sort using Kahn's Algorithm (BFS-based).
    Returns list of nodes in topological order.
    """
    in_degree = {u: 0 for u in graph}

    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        print("Cycle detected!")
        return []

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    print("Topological Order:", topological_sort_kahn(graph))

