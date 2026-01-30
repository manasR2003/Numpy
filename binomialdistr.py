#Binomial distribution
#it is also known as descrete distribution
#it is used for where it has 50-50 probability like coin toss
#it takes three argumenst 
#n= number of trails
#p= probability
#size= array size
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.binomial(n=10,p=0.5,size=10)
plt.plot(arr)
plt.show()
print(arr)