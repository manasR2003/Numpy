import numpy as np
#copy is used to copy the array and view is only for view the array
#in copy if we change the original array it will not effect the new array and vice versa
#in view if we change the original array it will effect the new array and vice versa

arr1=np.array([1,2,3,4,5,6])

arr2=arr1.copy()

print(arr1)
print(arr2)

arr1[0]=100

print(arr1)
print(arr2)

arr3=np.array([1,2,3,4,5,6])

arr4=arr3.view()

print(arr3)
print(arr4)

arr3[0]=100

print(arr3)
print(arr4)

#we can know that the copy and view owns the data or not by using "base"
#if it return an array means it doesnot owns the data and if it returns none means it owns the data

print(arr4.base)
print(arr2.base)

