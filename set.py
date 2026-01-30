import numpy as np

arr1=np.array([1,2,3,4,5,6,7,8,9,3,4,6,2,8])

arr2=np.unique(arr1)
print(arr2)

arr3=np.array([1,2,3,4,3,1])
arr4=np.array([9,8,7,6,3,2])

arr5=np.union1d(arr3,arr4)

print(arr5)

arr6=np.intersect1d(arr3,arr4)
print(arr6)

arr7=np.setdiff1d(arr3,arr4,assume_unique=True)
print(arr7)

arr8=np.setxor1d(arr3,arr4,assume_unique=True)
print(arr8)