import heapq

def prim(graph, start):
    """
    Prim's algorithm for Minimum Spanning Tree (MST).
    Returns list of edges in MST.
    """
    visited = set([start])
    edges = [
        (weight, start, to) for to, weight in graph[start].items()
    ]
    heapq.heapify(edges)
    mst = []

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))

    return mst

if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1},
        'C': {'A': 3, 'B': 1, 'D': 1},
        'D': {'B': 1, 'C': 1}
    }
    print("Edges in MST:", prim(graph, 'A'))
