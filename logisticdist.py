#Logistic distribution
# it is used for check the growth
#it also works like normal distribution
# argumensta also same as normal distribution
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.logistic(loc=10,scale=5,size=(20))
plt.plot(arr)
plt.show()
print(arr)