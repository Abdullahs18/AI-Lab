graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start, goal):
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            return True

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    print("\nGoal Not Found")
    return False

bfs(graph, 'A', 'F')
