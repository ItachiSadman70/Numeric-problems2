import matplotlib.pyplot as plt
def derivative_function(t, y):
    return y * (1 - y)
def euler_method(f, y0, t0, tn, h):
    t_values = [t0]
    y_values = [y0]

    while t_values[-1] < tn:
        t_next = t_values[-1] + h
        y_next = y_values[-1] + h * f(t_values[-1], y_values[-1])
        t_values.append(t_next)
        y_values.append(y_next)

    return t_values, y_values

initial_value_y = 0.5
initial_value_t = 0
final_value_t = 5
step_size = 0.1
t_values, y_values = euler_method(derivative_function, initial_value_y, initial_value_t, final_value_t, step_size)

plt.plot(t_values, y_values, label='Euler\'s Method')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Approximate Solution of dy/dt = y(1 - y) with y(0) = 0.5')
plt.legend()
plt.show()
