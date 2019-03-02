#this file will serve as a place to test graphs

import matplotlib.pyplot as plt
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

delay_tolerant_user1 = norm_log_util_function(set_rate,15)
plt.plot(set_rate,delay_tolerant_user1,label='delayed-user1')

delay_tolerant_user2 = norm_log_util_function(set_rate,0.1)
plt.plot(set_rate,delay_tolerant_user2,label='delayed-user2')


'''
  (b) plot  two  normalized  sigmoid  utility  functions  with a=  5  and b=  10,and a= 0.5 and b= 20.
      What is the change to the function with increase inthe value of a?  and increase in the value of b?

'''

# To represent real-time applications runningon mobile stations, use the normalized sigmoid utility function
# def norm_sigmoid_util_function(rate,ai,bi):
#     sig_container = []
#     for ri in rate:
#         # Ci = ((1 + math.exp(ai * bi))/math.exp(ai * bi))
#         # di = (1/(1 + math.exp(ai * bi)))
# 	    sig_container.append((((1 + math.exp(ai * bi))/math.exp(ai * bi)) * ((1/1 + math.exp(-ai(ri - bi)) - (1/(1 + math.exp(ai * bi)))))))
#     return sig_container

# realtime_user1 = norm_sigmoid_util_function(set_rate,5,10)
# plt.plot(set_rate,realtime_user1,label='realtime-user1')

# realtime_user2 = norm_sigmoid_util_function(set_rate,0.5,20)
# plt.plot(set_rate,realtime_user2,label='realtime-user2')


plt.xlabel('ri')
plt.ylabel('Ui(ri)')
plt.title('Assignment 1')
plt.legend()
plt.show()

