import math


def function_to_find_root(c):
    return (667.38 / c) * (1 - math.exp(-0.146843 * c)) - 40


def false_position_method(func, a, b, tol=1e-6, max_iter=100):

    if func(a) * func(b) > 0:
        raise ValueError("The function must have different signs at the interval endpoints.")

    iterations = 0
    while iterations < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if abs(func(c)) < tol:
            return c, iterations

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    raise ValueError("False-position method did not converge within the maximum number of iterations.")

x1 = 12
x2 = 16
tolerance = 1e-6

root, iterations = false_position_method(function_to_find_root, x1, x2, tol=tolerance)
print(f"Approximated root: {root:.6f}")
print(f"Iterations: {iterations}")
