import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt
import random 

x=sp.symbols('x')

y = x**4 - 4*x**3 + x
dy=sp.diff(y,x)

print(dy)

loss=sp.lambdify(x,y)
gradient=sp.lambdify(x,dy)

xval=np.linspace(-3.5,5.5,10000)
yval=loss(xval)
plt.plot(xval,yval)

def descent(x,u,itr):
    xg=[x]
    yg=[loss(x)]
    y=loss(x)
    for _ in range(itr):
        x = x - u * gradient(x)
        xg.append(x)
        yg.append(loss(x))
        plt.plot(xg,yg,marker="*",color=(random.random(), random.random(), random.random()))
descent(-2,0.01,300)
descent(2,0.01,100)
descent(0,0.1,100)

plt.show()
