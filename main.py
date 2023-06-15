import random

adjacency_matrix = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

colors = ['red', 'blue', 'green', 'yellow']
population_size = 1000


def graph_coloring(adjacency_matrix, colors):
    num_nodes = len(adjacency_matrix)

    population = [generate_random_coloring(num_nodes, colors) for i in range(population_size)]

    while True:
        fitness = [count_conflicts(member, adjacency_matrix) for member in population]

        if 0 in fitness:
            best_index = fitness.index(0)
            return population[best_index]

        parent1 = population[select_parent(fitness)]
        parent2 = population[select_parent(fitness)]

        crossover_point = random.randint(1, num_nodes - 1)
        offspring = parent1[:crossover_point] + parent2[crossover_point:]
        offspring_conflicts = count_conflicts(offspring, adjacency_matrix)

        least_fit_index = fitness.index(max(fitness))
        population[least_fit_index] = offspring

        population = mutate_coloring(population, colors)


def generate_random_coloring(num_nodes, colors):
    return [random.choice(colors) for i in range(num_nodes)]


def count_conflicts(member, adjacency_matrix):
    conflicts = 0
    num_nodes = len(member)

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i][j] and member[i] == member[j]:
                conflicts += 1

    return conflicts


def select_parent(fitness, k=3):
    selected = random.sample(range(len(fitness)), k)
    tournament_fitness = [fitness[i] for i in selected]
    best_index = selected[tournament_fitness.index(min(tournament_fitness))]

    return best_index


def mutate_coloring(population, colors):
    selected = random.sample(range(len(population)), 10 // len(population))
    mutated_population = population[:]
    num_nodes = len(mutated_population)
    for j in range(len(selected)):
        for i in range(num_nodes):
            if random.randint(0, 100) < 30:
                mutated_population[selected[j]][i] = random.choice(colors)

    return mutated_population


result = graph_coloring(adjacency_matrix, colors)
print(result)
