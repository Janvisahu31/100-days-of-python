def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    """
    Kruskal's algorithm for Minimum Spanning Tree (MST).
    Returns list of edges in MST.
    """
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent, rank = {}, {}

    for u, v, _ in graph:
        parent[u] = u
        parent[v] = v
        rank[u] = 0
        rank[v] = 0

    while e < len(parent) - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result

if __name__ == "__main__":
    edges = [
        ('A', 'B', 4),
        ('A', 'H', 8),
        ('B', 'H', 11),
        ('B', 'C', 8),
        ('C', 'D', 7),
        ('C', 'F', 4),
        ('D', 'E', 9),
        ('D', 'F', 14),
        ('E', 'F', 10),
        ('F', 'G', 2),
        ('G', 'H', 1),
        ('H', 'I', 7)
    ]
    print("Edges in MST:", kruskal(edges))
