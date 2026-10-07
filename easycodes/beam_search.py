graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}

def beam_search(graph, start, goal, beam_width):
    beam = [(0, [start])]

    while beam:
        candidates = []

        for cost, path in beam:
            node = path[-1]

            if node == goal:
                return path, cost

            for neighbor, weight in graph.get(node, []):
                new_cost = cost + weight
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))

        if not candidates:
            break

        candidates.sort()
        beam = candidates[:beam_width]

    return None, 0

path, cost = beam_search(graph, 'S', 'L', 3)

if path:
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
else:
    print("No path found")
