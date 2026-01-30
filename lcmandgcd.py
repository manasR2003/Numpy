import numpy as np

arr1=np.array([10,20,30])


arr3=np.lcm.reduce(arr1)
print(arr3)

arr4=np.arange(1,11)
print(np.lcm.reduce(arr4))

arr5=np.gcd.reduce(arr1)
print(arr5)

arr6=np.arange(1,11)
print(np.gcd.reduce(arr6))

