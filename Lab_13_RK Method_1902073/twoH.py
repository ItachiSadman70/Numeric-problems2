def runge_kutta_system(f, y0, v0, t0, tn, h):
    t_values = [t0]
    y_values = [y0]
    v_values = [v0]

    while t_values[-1] < tn:
        t = t_values[-1]
        y = y_values[-1]
        v = v_values[-1]

        k1_y = h * v
        k1_v = h * f(t, y, v)

        k2_y = h * (v + 0.5 * k1_v)
        k2_v = h * f(t + 0.5 * h, y + 0.5 * k1_y, v + 0.5 * k1_v)

        k3_y = h * (v + 0.5 * k2_v)
        k3_v = h * f(t + 0.5 * h, y + 0.5 * k2_y, v + 0.5 * k2_v)

        k4_y = h * (v + k3_v)
        k4_v = h * f(t + h, y + k3_y, v + k3_v)

        y_new = y + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6.0
        v_new = v + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6.0
        t_new = t + h

        t_values.append(t_new)
        y_values.append(y_new)
        v_values.append(v_new)

    return t_values, y_values, v_values

def my_first_ode(t, y, v):
    return v

def my_second_ode(t, y, v):
    return -2 * v - 2 * y

def main():
    # Set initial conditions and solve the system of ODEs
    y0 = 1.0
    v0 = 0.0
    t0 = 0.0
    tn = 5.0
    h = 0.1

    t_values, y_values, v_values = runge_kutta_system(my_first_ode, y0, v0, t0, tn, h)

    # Print the results
    print("Time\t\tValue of y\tValue of v")
    print("--------------------------------")
    for t, y, v in zip(t_values, y_values, v_values):
        print(f"{t:.2f}\t\t{y:.6f}\t\t{v:.6f}")

if __name__ == "__main__":
    main()
