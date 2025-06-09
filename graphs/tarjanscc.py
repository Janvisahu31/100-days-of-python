def tarjans_scc(graph):
    """
    Tarjan's Algorithm for finding SCCs.
    Returns list of SCCs.
    """
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = {}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in graph:
        if v not in indices:
            strongconnect(v)

    return sccs

if __name__ == "__main__":
    graph = {
        0: [1],
        1: [2, 4, 5],
        2: [3, 6],
        3: [2, 7],
        4: [0, 5],
        5: [6],
        6: [5],
        7: [3, 6]
    }
    print("SCCs:", tarjans_scc(graph))
