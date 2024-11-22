import numpy as np

# Coefficients matrix
coefficients = np.array([[1, 1, 1],
                         [2, 3, 6],
                         [1, 1, -1]])

# Constants on the right-hand side
constants = np.array([8500, 38000, 0])

# Calculate the determinant of the coefficient matrix
det_coefficients = np.linalg.det(coefficients)

# Create copies of the coefficients matrix and replace columns with constants
coefficients_x = coefficients.copy()
coefficients_x[:, 0] = constants

coefficients_y = coefficients.copy()
coefficients_y[:, 1] = constants

coefficients_z = coefficients.copy()
coefficients_z[:, 2] = constants

# Calculate the determinants of the modified matrices
det_x = np.linalg.det(coefficients_x)
det_y = np.linalg.det(coefficients_y)
det_z = np.linalg.det(coefficients_z)

# Use Cramer's rule to find the solutions
solution_x = det_x / det_coefficients
solution_y = det_y / det_coefficients
solution_z = det_z / det_coefficients

print("Solution:")
print(f"x = {solution_x}")
print(f"y = {solution_y}")
print(f"z = {solution_z}")
