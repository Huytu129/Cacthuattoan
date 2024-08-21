import random
import math

def simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, iteration_limit):
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    best_solution = current_solution
    best_value = current_value

    for iteration in range(iteration_limit):
        # Tạo ra giải pháp lân cận (neighbor)
        neighbor_solution = current_solution + random.uniform(-1, 1)
        neighbor_value = objective_function(neighbor_solution)

        # Chấp nhận giải pháp lân cận nếu nó tốt hơn hoặc với xác suất giảm dần theo nhiệt độ
        if neighbor_value < current_value or random.random() < math.exp((current_value - neighbor_value) / temperature):
            current_solution = neighbor_solution
            current_value = neighbor_value

            if current_value < best_value:
                best_solution = current_solution
                best_value = current_value

        # Giảm nhiệt độ theo hệ số làm mát
        temperature *= cooling_rate

    return best_solution, best_value

# Example usage: Tìm giá trị nhỏ nhất của hàm f(x) = (x-3)^2
def objective_function(x):
    return (x - 3) ** 2

initial_solution = random.uniform(-10, 10)
temperature = 1000
cooling_rate = 0.95
iteration_limit = 1000

best_solution, best_value = simulated_annealing(objective_function, initial_solution, temperature, cooling_rate, iteration_limit)
print(f"Best solution: {best_solution}, Best value: {best_value}")
