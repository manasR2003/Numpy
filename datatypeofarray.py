import numpy as np

#we can find out the data type of an array by using "dtype"

arr=np.array([1,2,3,4,5])
print(arr.dtype)
arr1=np.array(['manas','ranjan'])
print(arr1.dtype)
arr2=np.array([True,False,False,True])
print(arr2.dtype)

#we can also defined the types of data at the time of creation by using "dtype"

arr3=np.array([1,2,3,4],dtype='S')
print(arr3)
print(arr3.dtype)

#we can also convert the types of data from the existing array by using "astype" in a new memory location
#it will be work on only homogeneous datatype only
arr4=np.array([10,20,30,40,50])
arr5=arr4.astype('S')
print(arr5)
print(arr5.dtype)