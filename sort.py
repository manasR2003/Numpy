import numpy as np

#sorting can be done by using sort() which makes changes in existing array
arr1=np.array([4,1,6,3,8,4,5,6,7,77,89,5,4,32,44])
arr2=np.sort(arr1)
print(arr2)

arr = np.array(['banana', 'cherry', 'apple'])
arr3=np.sort(arr)
print(arr3)

arr = np.array([True, False, True])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
