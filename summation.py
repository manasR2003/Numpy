import numpy as np

arr1=np.array([10,20,30])
arr2=np.array([40,50,60])

arr=np.sum([arr1,arr2])
arr3=np.sum([arr1,arr2],axis=1)
print(arr)
print(arr3)

arr4=np.cumsum(arr2)
print(arr4)