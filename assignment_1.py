# This file will serve as a place to test graphs


import numpy as np
import math

'''
 (a) Plot two normalized logarithmic utility functions with k = 15
     and r-max = 50, and k = 0.1 and r-max = 50
'''
# Define Rate Set (50 being maximum required rate for the user to achieve 100%
set_rate = np.arange(0.,49.,0.1)

# to represent delay-tolerant applications running on mobilestations, use the normalized logarithmic utility function
def norm_log_util_function(rate,rate_of_utilization):
    container = []
    for ri in rate:
        container.append(math.log(1 + (rate_of_utilization * ri))/(math.log(1 + (rate_of_utilization * max(rate)))))

    return container
normalized = norm_log_util_function(set_rate,15)
#print(normalized)

import matplotlib.pyplot as plt
plt.plot(set_rate,normalized)
plt.xlabel('rate')
plt.ylabel('utilization')
plt.show()

