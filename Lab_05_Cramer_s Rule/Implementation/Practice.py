import numpy as np

coefficients = np.array([[1, 1, 1], [2, 3, 6], [1, 1, -1]])
constants = np.array([8500, 38000, 0])

det_coefficents = np.linalg.det(coefficients)

coefficients_x = coefficients.copy()
coefficients_x[:, 0] = constants

coefficients_y = coefficients.copy()
coefficients_y[:, 1] = constants

coefficients_z = coefficients.copy()
coefficients_z[:, 2] = constants

det_x=np.linalg.det(coefficients_x)
det_y=np.linalg.det(coefficients_y)
det_z=np.linalg.det(coefficients_z)

solution_x=det_x/det_coefficents
solution_y=det_y/det_coefficents
solution_z=det_z/det_coefficents

print("Solution;")
print(f"x={solution_x}")
print(f"y={solution_y}")
print(f"z={solution_z}")
