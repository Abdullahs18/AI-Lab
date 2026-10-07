graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 0,
    'E': 3,
    'F': 1
}

def greedy_bfs(graph, start, goal):
    frontier = [(heuristic[start], start)]
    visited = []

    while frontier:
        frontier.sort()
        h, node = frontier.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            return

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                frontier.append((heuristic[neighbor], neighbor))

    print("\nGoal Not Found")

greedy_bfs(graph, 'A', 'F')
