from scipy.optimize import linear_sum_assignment
import numpy as np

def hungarian_algorithm(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind, cost_matrix[row_ind, col_ind].sum()

# Example usage:
cost_matrix = np.array([
    [4, 1, 3],
    [2, 0, 5],
    [3, 2, 2]
])

row_ind, col_ind, total_cost = hungarian_algorithm(cost_matrix)
print(f"Optimal assignment: {list(zip(row_ind, col_ind))}")
print(f"Total cost: {total_cost}")
