# uniform distribution
# it is Used to describe probability where every event has equal chances of occuring.
# it takes 3 arguments
# low=0.0
# high=1.0
# size=array size
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.uniform(size=20)
plt.plot(arr)
plt.show()
print(arr)