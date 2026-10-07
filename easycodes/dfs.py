graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, start, goal):
    stack = [start]
    visited = [start]

    while stack:
        node = stack.pop()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found")
            return True

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

    print("\nGoal Not Found")
    return False

dfs(graph, 'A', 'F')
