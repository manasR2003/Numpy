import numpy as np

#we can find the shape of an array by using "shape"

arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2],[3,4],[5,6]])
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

#it will return the tuple of rows number and elements
#we can reshape the array by using "reshape"

arr4=arr2.reshape(2,3)
print(arr4)
print(arr4.shape)

arr5=arr3.reshape(2,-1)#here -1 will calculate the element automatically
print(arr5)

arr6=arr3.reshape(-1)#it will convert to 1 dimensional array
print(arr6)