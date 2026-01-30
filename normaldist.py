#Normal distributaion 
#it is also known as gussian distribution.
#it is mainly used for check IQ score and heart beat
#it takes 3 arguments which is 
# loc=mean
# scale= deviations
# size= array size

import numpy as np
import matplotlib.pyplot as plt
from numpy import random

arr=random.normal(loc=10,scale=5,size=(20))
plt.plot(arr)
plt.show()
print(arr)