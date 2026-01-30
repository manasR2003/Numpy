import numpy as np

arr1=np.array([1,2,3,4,5,6])
arr2=np.array([[1,2],[3,4],[5,6],[7,8]])
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

arr4=np.split(arr1,3)
print(arr4)

arr5=np.split(arr2,2)
print(arr5)

arr6=np.split(arr3,2)
print(arr6)