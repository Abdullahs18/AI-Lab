graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

def dls(graph, node, goal, depth, limit, path):
    if node == goal:
        return path

    if depth == limit:
        return None

    for neighbor in graph.get(node, []):
        if neighbor not in path:
            new_path = path + [neighbor]
            result = dls(graph, neighbor, goal, depth + 1, limit, new_path)

            if result is not None:
                return result

    return None

path = dls(graph, 'A', 'G', 0, 3, ['A'])

if path:
    print("Path:", " -> ".join(path))
else:
    print("Goal Not Found")
