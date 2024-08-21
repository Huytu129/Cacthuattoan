import random

def genetic_algorithm(objective_function, bounds, population_size, generations, mutation_rate):
    def create_individual(bounds):
        return [random.uniform(bound[0], bound[1]) for bound in bounds]

    def mutate(individual, bounds, mutation_rate):
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                individual[i] = random.uniform(bounds[i][0], bounds[i][1])

    def crossover(parent1, parent2):
        if len(parent1) < 2:
            return parent1[:], parent2[:]  # Không thể thực hiện crossover nếu độ dài cá thể nhỏ hơn 2
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        return offspring1, offspring2

    def select(population, num=2):
        # Chọn num cá thể tốt nhất từ quần thể
        sorted_population = sorted(population, key=lambda x: objective_function(x))
        return sorted_population[:num]

    # Khởi tạo quần thể
    population = [create_individual(bounds) for _ in range(population_size)]

    # Chạy thuật toán qua nhiều thế hệ
    for generation in range(generations):
        new_population = []
        while len(new_population) < population_size:
            parents = select(population, num=2)
            parent1, parent2 = parents[0], parents[1]
            offspring1, offspring2 = crossover(parent1, parent2)
            mutate(offspring1, bounds, mutation_rate)
            mutate(offspring2, bounds, mutation_rate)
            new_population.extend([offspring1, offspring2])

        population = new_population[:population_size]  # Đảm bảo kích thước quần thể không thay đổi

    # Tìm nghiệm tốt nhất trong quần thể
    best_individual = select(population, num=1)[0]
    return best_individual, objective_function(best_individual)

# Example usage: Tìm giá trị nhỏ nhất của hàm f(x) = (x-3)^2 với quần thể ban đầu
def objective_function(individual):
    x = individual[0]
    return (x - 3) ** 2

bounds = [(-10, 10)]
population_size = 100
generations = 50
mutation_rate = 0.1

best_individual, best_value = genetic_algorithm(objective_function, bounds, population_size, generations, mutation_rate)
print(f"Best individual: {best_individual}, Best value: {best_value}")
