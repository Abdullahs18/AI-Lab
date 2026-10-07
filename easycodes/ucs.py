graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4), ('E', 3)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(graph, start, goal):
    queue = [(0, start)]
    cost = {start: 0}
    visited = []

    while queue:
        queue.sort()
        current_cost, node = queue.pop(0)

        if node in visited:
            continue

        visited.append(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            print("Cost:", current_cost)
            return

        for neighbor, weight in graph.get(node, []):
            new_cost = current_cost + weight

            if new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                queue.append((new_cost, neighbor))

    print("\nGoal Not Found")

ucs(graph, 'A', 'F')
