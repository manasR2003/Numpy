# exponential distribution
# it is used to check the time till the next event
# it takes 2 argumenst
# scale=default 1.0
# size=array size
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.exponential(size=10)
plt.plot(arr)
plt.show()
print(arr)
