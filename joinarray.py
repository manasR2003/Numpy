import numpy as np

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

arr=np.hstack([arr1,arr2])
#print(arr)

arr3=np.vstack([arr1,arr2])
#print(arr3)

arr4=np.dstack([arr1,arr2])
#print(arr4)

arr5=np.array([[1,2],[3,4]])
arr6=np.array([[5,6],[7,8]])

arr7=np.hstack([arr5,arr6])
print(arr7)

arr8=np.vstack([arr5,arr6])
print(arr8)

arr9=np.dstack([arr5,arr6])
print(arr9)


#same as different dimension array can join by using "hstack","vstack" and "dtsack".