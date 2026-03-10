import numpy as np
import matplotlib.pyplot as plt


r_min = 2.5
r_max = 4.0
r_values = np.linspace(r_min, r_max, 10000)
iterations = 1000
last = 100


x = 1e-5 * np.ones(len(r_values))

# Create the plot
plt.figure(figsize=(10, 7))
for i in range(iterations):
    x = r_values * x * (1 - x)
    if i >= (iterations - last):
        plt.plot(r_values, x, ',k', alpha=0.25)
        
plt.title('Bifurcation diagram')
plt.xlabel('r')
plt.ylabel('x')
plt.show()
