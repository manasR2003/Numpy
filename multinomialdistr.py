#Multinomial distribution
#it is the generailiesd of binomial distribution
#it is used where there is outcomes of multi-nomial scenarios.
#it is also takes three arguments
#n=number of trails
#pvals=probabilites for each trails
#size=array size
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.multinomial(n=2,pvals=[0.5,0.5],size=10)
plt.plot(arr)
plt.show()
print(arr)