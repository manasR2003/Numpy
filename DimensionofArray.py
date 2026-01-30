import numpy as np
#we can defined the dimension of an array by using "ndim"

arr1=np.array([1,2,3,4,5]) #all element are 0dimensional
arr2=np.array([[1,2],[3,4]])#all elemenets are 1dimensional
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])#all elements are 2dimensional

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#we can also create different dimensional at the time array creation by using "ndmin"

arr4=np.array([1,2,3,4,5],ndmin=2)
arr5=np.array([1,2,3,4,5,6,7,8,9],ndmin=10)

print(arr4)
print(arr4.ndim)

print(arr5)
print(arr5.ndim)