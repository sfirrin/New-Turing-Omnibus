import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

corna = 10
cornb = 10
side = 20
x_values = []
y_values = []


for i in range(1, 101):
    for j in range(1, 101):
        x = corna + i*side/100
        y = cornb + j*side/100
        c = int(x**2 + y**2)
        
        if (c%2 == 0):
            x_values.append(x)
            y_values.append(y)

plt.plot(x_values, y_values, 'bs', marker='.')
plt.axis('off')
plt.show()
