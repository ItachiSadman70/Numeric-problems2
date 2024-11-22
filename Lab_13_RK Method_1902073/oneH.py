def runge_kutta(f, y0, t0, tn, h):
    t_values = [t0]
    y_values = [y0]

    while t_values[-1] < tn:
        t = t_values[-1]
        y = y_values[-1]

        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)

        y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t_new = t + h

        t_values.append(t_new)
        y_values.append(y_new)

    return t_values, y_values

def my_ode(t, y):
    return -y

def main():
    # Set initial conditions and solve the ODE
    y0 = 1.0
    t0 = 0.0
    tn = 5.0
    h = 0.1

    t_values, y_values = runge_kutta(my_ode, y0, t0, tn, h)

    # Print the results
    print("Time\t\tValue of y")
    print("-----------------------")
    for t, y in zip(t_values, y_values):
        print(f"{t:.2f}\t\t{y:.6f}")

if __name__ == "__main__":
    main()
