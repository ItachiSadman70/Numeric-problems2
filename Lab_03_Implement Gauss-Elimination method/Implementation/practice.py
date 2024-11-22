import numpy as np

coefficients = np.array([[3, .1, -0.2], [0.1, 7, -0.3], [0.3, -2, 10]])
constants = np.array([7.85, -19.3, 71.4])

aug_matrix = np.column_stack((coefficients, constants))
n = len(constants)
for i in range(n):
    aug_matrix[i, :] = aug_matrix[i, :] / aug_matrix[i, i]
    for j in range(n):
        if i != j:
            aug_matrix[j, :] -= aug_matrix[j, i] * aug_matrix[i, :]
solutions = aug_matrix[:, -1]
print("x=", solutions[0])
print("y=", solutions[1])
print("z=", solutions[2])
