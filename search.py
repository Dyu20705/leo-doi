import heapq

def climb_hill(start, goal, graph):
    if start not in graph:
        return [], []

    L = []
    path = []
    steps = []
    expanded = set()

    heapq.heappush(L, (graph[start][0], start))

    while L:
        _, cur = heapq.heappop(L)

        if cur in expanded:
            continue

        expanded.add(cur)
        path.append(cur)

        if cur == goal:
            return path, steps

        LA = []
        neighbors = graph.get(cur, (None, []))[1]

        for neighbor in neighbors:
            if neighbor in graph and neighbor not in expanded:
                heapq.heappush(LA, (graph[neighbor][0], neighbor))

        la_nodes = [n for _, n in sorted(LA)]
        while LA:
            heapq.heappush(L, heapq.heappop(LA))

        steps.append({
            "current": cur,
            "neighbors": neighbors,
            "L1": la_nodes,
            "L": [n for _, n in L]
        })

    return path, steps