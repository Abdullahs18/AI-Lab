import random

n = 4
population_size = 10
mutation_rate = 0.1

def fitness(state):
    conflicts = 0

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return 1 / (1 + conflicts)

def create_individual():
    return random.sample(range(n), n)

def create_population():
    population = []

    for i in range(population_size):
        population.append(create_individual())

    return population

def select_parents(population):
    population.sort(key=fitness, reverse=True)
    return population[:population_size // 2]

def crossover(parent1, parent2):
    point = n // 2
    child = parent1[:point] + parent2[point:]

    # Repair duplicate columns simply
    used = []
    missing = []

    for i in range(n):
        if child[i] in used:
            missing.append(child[i])
        else:
            used.append(child[i])

    available = []

    for x in range(n):
        if x not in child:
            available.append(x)

    for i in range(n):
        if child.count(child[i]) > 1:
            if available:
                child[i] = available.pop(0)

    return child

def mutate(child):
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)

    child[a], child[b] = child[b], child[a]
    return child

def genetic_algorithm():
    population = create_population()

    for generation in range(100):
        best = population[0]

        for individual in population:
            if fitness(individual) > fitness(best):
                best = individual

        print("Generation:", generation, "Best Fitness:", fitness(best))

        if fitness(best) == 1.0:
            return best

        parents = select_parents(population)
        new_population = []

        while len(new_population) < population_size:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)

            child = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                child = mutate(child)

            new_population.append(child)

        population = new_population

    return best

solution = genetic_algorithm()

print("Best Solution:", solution)
print("Fitness:", fitness(solution))
