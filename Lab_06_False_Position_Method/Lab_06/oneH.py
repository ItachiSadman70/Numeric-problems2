import matplotlib.pyplot as plt
from tabulate import tabulate

def false_position_method(func, a, b, tol=0.01, max_iter=100):
    iterations = []
    a_values = []
    b_values = []
    c_values = []
    f_a_values = []
    f_b_values = []
    f_c_values = []

    if func(a) * func(b) > 0:
        raise ValueError("The function must have different signs at the interval endpoints.")

    for i in range(max_iter):
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        iterations.append(i)
        a_values.append(a)
        b_values.append(b)
        c_values.append(c)
        f_a = func(a)
        f_b = func(b)
        f_c = func(c)
        f_a_values.append(f_a)
        f_b_values.append(f_b)
        f_c_values.append(f_c)

        if abs(func(c)) < tol:
            break

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    results = list(zip(iterations, a_values, b_values, c_values, f_a_values, f_b_values, f_c_values))
    table = tabulate(results,
                     headers=["Iteration", "a", "b", "c", "f(a)", "f(b)", "f(c)"],
                     tablefmt="pretty")

    x = [i / 10 for i in range(int(10 * min(a, b)) - 1, int(10 * max(a, b)) + 2)]
    y = [func(xi) for xi in x]

    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='red', linestyle='--', label='y=0')
    plt.axvline(c, color='green', linestyle='--', label='Root Approximation')

    plt.title('False-Position Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(table)

    return c

# Example usage:
def example_function(x):
    return x**2-3

a = 1
b = 2
tolerance = 0.01

root = false_position_method(example_function, a, b, tol=tolerance)
print(f"Approximated root: {root:.6f}")
