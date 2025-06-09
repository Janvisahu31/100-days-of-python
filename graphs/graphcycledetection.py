def is_cyclic_util(graph, v, visited, parent):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if is_cyclic_util(graph, neighbor, visited, v):
                return True
        elif parent != neighbor:
            return True

    return False

def is_cyclic(graph):
    """
    Cycle Detection in Undirected Graph.
    Returns True if cycle exists, else False.
    """
    visited = {v: False for v in graph}

    for vertex in graph:
        if not visited[vertex]:
            if is_cyclic_util(graph, vertex, visited, -1):
                return True
    return False

if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 4],
        4: [3]
    }
    print("Graph contains cycle:" if is_cyclic(graph) else "Graph does not contain cycle.")
