def conflicts(state):
    count = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                count += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                count += 1

    return count

def get_neighbors(state):
    neighbors = []
    n = len(state)

    for row in range(n):
        for col in range(n):
            if col != state[row]:
                new_state = state.copy()
                new_state[row] = col
                neighbors.append(new_state)

    return neighbors

def hill_climbing(start):
    current = start

    while True:
        current_score = conflicts(current)
        moved = False

        for neighbor in get_neighbors(current):
            neighbor_score = conflicts(neighbor)

            if neighbor_score < current_score:
                current = neighbor
                moved = True
                break

        if moved == False:
            return current, conflicts(current)

solution, score = hill_climbing([0, 1, 2, 3])

print("Solution:", solution)
print("Conflicts:", score)
