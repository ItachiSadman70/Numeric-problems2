import numpy as np
coefficients = np.array([[10, 20], [1, 1]])

constants = np.array([50, 3])

augmented_matrix = np.column_stack((coefficients, constants))

n = len(constants)

for i in range(n):
    augmented_matrix[i, :] = augmented_matrix[i, :] / augmented_matrix[i, i]

    for j in range(n):
        if i != j:
            augmented_matrix[j, :] -= augmented_matrix[j, i] * augmented_matrix[i, :]

solutions = augmented_matrix[:, -1]

print("Number of T-shirts (x):", solutions[0])
print("Number of Hoodies (y):", solutions[1])
