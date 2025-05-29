from collections import deque

def bfs_farthest_node(graph, start): #funkcija toliamiausiui mazgui nuo virsunes surast
    visited = {start}
    queue = deque([(start, 0)])
    farthest_node = start
    max_dist = 0
    parents = {start: None}

    while queue:
        node, dist = queue.popleft()
        if dist > max_dist:
            max_dist = dist
            farthest_node = node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = node
                queue.append((neighbor, dist + 1))

    return farthest_node, parents


def find_tree_center(graph):
    # Step 1: find one end of diameter
    u, _ = bfs_farthest_node(graph, start=list(graph.keys())[0])

    # Step 2: find other end and path from u
    v, parents = bfs_farthest_node(graph, start=u)

    # Step 3: construct diameter path
    path = []
    while v is not None:
        path.append(v)
        v = parents[v]
    path.reverse()

    # Step 4: return center(s)
    n = len(path)
    if n % 2 == 1:
        return [path[n // 2]]
    else:
        return [path[n // 2 - 1], path[n // 2]]


# Pavyzdys:
# Medis kaip adjacency sąrašas
tree = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1, 4, 5],
    4: [3],
    5: [3]
}

print("Medzio centras (-ai):", find_tree_center(tree))
