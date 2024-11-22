import numpy as np
coefficients = np.array([[0.3, 0.52, 1],
                         [0.5, 0.3, 0.5],
                         [0.1, 0.3, 0.5]])

constants = np.array([0.01, 0.67, -0.44])

det_coefficients = np.linalg.det(coefficients)

coefficients_x = coefficients.copy()
coefficients_x[:, 0] = constants

coefficients_y = coefficients.copy()
coefficients_y[:, 1] = constants

coefficients_z = coefficients.copy()
coefficients_z[:, 2] = constants

det_x = np.linalg.det(coefficients_x)
det_y = np.linalg.det(coefficients_y)
det_z = np.linalg.det(coefficients_z)


solution_x = det_x / det_coefficients
solution_y = det_y / det_coefficients
solution_z = det_z / det_coefficients

print("Solution:")
print(f"x = {solution_x}")
print(f"y = {solution_y}")
print(f"z = {solution_z}")
