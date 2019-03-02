# This file will serve as a place to test graphs

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-8,8,0.1)
f = 1 / (1 + np.exp(-x))

plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

