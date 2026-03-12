import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# define symbols
x, y, v = sp.symbols('x y v')

# define your 2nd order ODE here , change this line for any equation

expr = y 

# auto differentiate to get the system
f2_sym = expr
f1_sym = v  # dy/dx = v always
 
 
f1 = sp.lambdify((x, y, v), f1_sym)
f2 = sp.lambdify((x, y, v), f2_sym)

def rk4_2nd(h, a, xi, yi, vi):
    steps = int(abs(a - xi) / h)
    x_val = xi
    y_val = yi
    v_val = vi
    xl = [x_val]
    yl = [y_val]

    for _ in range(steps):
        k1y = f1(x_val, y_val, v_val)
        k1v = f2(x_val, y_val, v_val)

        k2y = f1(x_val + h/2, y_val + h/2 * k1y, v_val + h/2 * k1v)
        k2v = f2(x_val + h/2, y_val + h/2 * k1y, v_val + h/2 * k1v)

        k3y = f1(x_val + h/2, y_val + h/2 * k2y, v_val + h/2 * k2v)
        k3v = f2(x_val + h/2, y_val + h/2 * k2y, v_val + h/2 * k2v)

        k4y = f1(x_val + h, y_val + h * k3y, v_val + h * k3v)
        k4v = f2(x_val + h, y_val + h * k3y, v_val + h * k3v)

        y_val = y_val + (h/6) * (k1y + 2*k2y + 2*k3y + k4y)
        v_val = v_val + (h/6) * (k1v + 2*k2v + 2*k3v + k4v)
        x_val = x_val + h
        xl.append(x_val)
        yl.append(y_val)

    return xl, yl

xl, yl = rk4_2nd(0.1, 1000, 100, 1, 1)



plt.plot(xl, yl, label='RK4', linewidth=2)
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('2nd Order ODE Solver')
plt.show()