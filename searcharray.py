import numpy as np

#in this method it returns all index value only.
arr1=np.array([1,2,3,4,5,6,7,8])

arr2=np.where(arr1==8)
print(arr2)

arr3=np.where(arr1%2==0)
print(arr3)

x=np.where(arr1==9)
print(x)

z=np.searchsorted(arr1,7)
print(z)

y=np.searchsorted(arr1,[9,10,11])
print(y)