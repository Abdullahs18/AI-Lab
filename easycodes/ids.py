tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

def dls(node, goal, depth, path):
    if node == goal:
        path.append(node)
        return True

    if depth == 0:
        return False

    for child in tree.get(node, []):
        if child not in path:
            if dls(child, goal, depth - 1, path):
                path.append(node)
                return True

    return False

def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []

        if dls(start, goal, depth, path):
            path.reverse()
            print("Path:", " -> ".join(path))
            return True

    print("Goal Not Found")
    return False

ids('A', 'G', 4)
