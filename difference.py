import numpy as np
arr=np.array([40,50,60])

arr1=np.diff(arr)
print(arr1)

arr2=np.diff(arr,n=2)
print(arr2)