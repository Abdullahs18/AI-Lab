graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 3)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 2,
    'E': 1,
    'F': 0
}

def a_star(graph, start, goal):
    queue = [(heuristic[start], 0, start)]
    cost = {start: 0}
    visited = []

    while queue:
        queue.sort()
        f, g, node = queue.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            print("Cost:", g)
            return

        for neighbor, weight in graph.get(node, []):
            new_g = g + weight
            new_f = new_g + heuristic[neighbor]

            if new_g < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_g
                queue.append((new_f, new_g, neighbor))

    print("\nGoal Not Found")

a_star(graph, 'A', 'F')
