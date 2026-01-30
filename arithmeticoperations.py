import numpy as np

#addition
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

arr=np.add(arr1,arr2)
print(arr)

#subtraction
arr3=np.subtract(arr2,arr1)
print(arr3)

#multiplication
arr4=np.multiply(arr1,arr2)
print(arr4)

#division
arr5=np.divide(arr1,arr2)
print(arr5)

#remainder
arr6=np.mod(arr2,arr1)
print(arr6)

#divmod
arr7=np.divmod(arr2,arr1)
print(arr7)

#power
arr8=np.power(arr2,arr1)
print(arr8)

#absolute value
arr9=np.array([-1,-3.3,-2,-0.5,0,3])
arr10=np.abs(arr9)
print(arr10)