import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2],[3,4]])
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#for one dimensional
print(arr1[0])
print(arr1[-2])

#for 2 dimensional
print(arr2[0][1])
print(arr2[-1][-2])

#for 3 dimensional
print(arr3[0][0][1])
print(arr3[-2][-1][-2])
