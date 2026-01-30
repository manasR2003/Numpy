import numpy as np
arr=np.array([40,50,60])
arr1=np.array([10,20,30])
arr2=np.prod([arr1,arr])
print(arr2)

arr3=np.prod(arr)
print(arr3)

arr4=np.prod([arr,arr1],axis=1)
print(arr4)

arr5=np.cumprod(arr)
print(arr5)