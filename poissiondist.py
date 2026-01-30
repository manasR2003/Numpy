#poission distribution
#it is used to check how many event occure in a specific time.
#it takes two arguments
#lam=number of occurrences
#size=array size
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.poisson(lam=2,size=10)
plt.plot(arr)
plt.show()
print(arr)