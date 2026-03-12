import numpy as np
import matplotlib.pyplot as plt
import math

"""numerical value finder in ode using euler method and RK4 """

def f(x,y):
    return -2*y

def euler(h,a,xi,yi):
    global xl,yl
    """f(x,y)=dy/dx , and f(x,y)=f for short , so put the first order differential equation in that form 
        when putting values in euler function :) , h is the step , and a is the value of x at which we 
        want to calculate the value of y , xi and yi being the initial x and y value at xi"""
    
    """ fi is the slope at current point, using it to step forward
        steps tells us how many times to iterate based on h"""
    
    steps=int(abs(a-xi)/h)
    x=xi
    y=yi
    fi=f(xi,yi)
    xl=[xi]
    yl=[yi]
    for _ in range(steps):
        x=x+h
        y=y+h*(fi)
        fi=f(x,y)
        xl.append(x)
        yl.append(y)
    print(x,"  ",y)  


def rk4(h, a, xi, yi):
    global xr,yr
    steps = int(abs(a - xi) / h)
    x = xi
    y = yi
    xr = [xi]
    yr = [yi]
    
    for _ in range(steps):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h,   y + h * k3)
        
        y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        xr.append(x)
        yr.append(y)
    print(x,"  ",y) 
    

euler(1,10,1,2)    
rk4(1,10,1,2)

"""plots for comparision"""
plt.plot(xl, yl, label='Euler')
plt.plot(xr, yr, label='RK4')
plt.legend()
plt.show()
    
