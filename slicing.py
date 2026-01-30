import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2],[3,4]])
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#for 1 dimensional
print(arr1[0:4])
print(arr1[:7:2])
print(arr1[-1:-5:-1])
print(arr1[::-1])

#for 2 dimensional
print(arr2[0:2,0:3])
print(arr2[1,0:3])
print(arr2[-1:-3:-1,-1:-3:-1])

#for 3 dimensional
print(arr3[0,0,1:2])
print(arr3[-1:-3:-1,-2:-3:-1,-1:-2:-1])