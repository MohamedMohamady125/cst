# CST-305 Project 2 – Classical RK4 + Euler comparison
# Programmers: Andres Reyes, Mohamed Mohamady
# ODE: y' = y / (e^x - 1),  initial condition: y(1) = 5
# Short run: 5 RK4 steps for the report table
# Long run: (N_LONG)1500 steps to measure time and compare RK4 vs Euler accuracy

from math import exp
from time import perf_counter

# ---------------------------
# Problem setup
X0 = 1.0      # starting x
Y0 = 5.0      # starting y
H_SHORT = 0.02
N_SHORT = 5   # number of RK4 steps for the table

H_LONG = 0.003
N_LONG = 1500 # assignment asks for ~1,000–2,000 points

RUN_SHORT = True   # print the 5-step RK4 table.... displayed on word document
RUN_LONG  = True   # run ~1500 steps and compare RK4 vs Euler
# ---------------------------

# ODE as a function: y' = f(x, y)
def f(x, y):
    # This is the formula
    return y / (exp(x) - 1.0)

# True (exact) solution: used as an "answer key" to check error
def y_true(x):
    # Derived earlier: y(x) = 5 * (1 - e^{-x}) / (1 - e^{-1})
    return 5.0 * (1.0 - exp(-x)) / (1.0 - exp(-1.0))

# One RK4 step (uses 4 internal slopes: k1, k2, k3, k4)
def rk4_step(x, y, h):
    # k-values are "slopes" sampled inside this single update
    k1 = f(x, y)
    k2 = f(x + h/2.0, y + (h/2.0) * k1)
    k3 = f(x + h/2.0, y + (h/2.0) * k2)
    k4 = f(x + h,     y + h * k3)

    # combine the 4 slopes to get the next y
    y_next = y + (h/6.0) * (k1 + 2*k2 + 2*k3 + k4)
    x_next = x + h
    return x_next, y_next, (k1, k2, k3, k4)

# One Euler step
def euler_step(x, y, h):
    # uses the slope only at the start of the interval
    y_next = y + h * f(x, y)
    x_next = x + h
    return x_next, y_next

# Print the 5-step RK4 table with k1..k4 and the true solution
def run_short():
    x, y = X0, Y0
    h = H_SHORT
    #
    print("i   x_i       y_i (RK4)   k1        k2       k3        k4       True y(x)")
    print(f"0   {x:.5f}   {y:.5f}     ----      ----     ----      ----     {y_true(x):.5f}")
    for i in range(1, N_SHORT + 1):
        x, y, (k1, k2, k3, k4) = rk4_step(x, y, h)
        print(f"{i}   {x:.5f}   {y:.5f}   {k1:.5f}   {k2:.5f}   {k3:.5f}   {k4:.5f}   {y_true(x):.5f}")

# Long run for performance and accuracy comparison (RK4 vs Euler)
def run_long():
    # RK4 stream
    x_rk4, y_rk4 = X0, Y0
    h = H_LONG
    t0 = perf_counter()
    for _ in range(N_LONG):
        x_rk4, y_rk4, _ = rk4_step(x_rk4, y_rk4, h)
    t1 = perf_counter()
    rk4_time = t1 - t0
    rk4_err = abs(y_rk4 - y_true(x_rk4))

    #Euler stream (same number of steps and same h)
    x_eu, y_eu = X0, Y0
    t2 = perf_counter()
    for _ in range(N_LONG):
        x_eu, y_eu = euler_step(x_eu, y_eu, h)
    t3 = perf_counter()
    eu_time = t3 - t2
    eu_err = abs(y_eu - y_true(x_eu))

    # Summary printout
    print("\nLong run summary (~{} points, h={}):".format(N_LONG, H_LONG))
    print(f"RK4   -> end x={x_rk4:.6f}, y={y_rk4:.6f}, true={y_true(x_rk4):.6f}, abs_err={rk4_err:.6e}, time_sec={rk4_time:.6f}")
    print(f"Euler -> end x={x_eu:.6f}, y={y_eu:.6f}, true={y_true(x_eu):.6f}, abs_err={eu_err:.6e}, time_sec={eu_time:.6f}")

if __name__ == "__main__":
    if RUN_SHORT:
        run_short()
    if RUN_LONG:
        run_long()
