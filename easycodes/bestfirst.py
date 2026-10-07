graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def best_first(graph, start, goal):
    queue = [(0, start)]
    visited = []

    while queue:
        queue.sort()
        value, node = queue.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            return

        for neighbor, value in graph.get(node, []):
            if neighbor not in visited:
                queue.append((value, neighbor))

    print("\nGoal Not Found")

best_first(graph, 'A', 'D')
