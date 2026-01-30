import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2],[3,4]])
arr3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#for 1D
for ele in arr1:
    print(ele)

#for 2D
for ele1 in arr2:
    for ele2 in ele1:
        print(ele2)

#for 3D
for ele1 in arr3:
    for ele2 in ele1:
        for ele3 in ele2:
            print(ele3)

#we have a method which iterate elements in single loop
#for 2D
for ele in np.nditer(arr2):
    print(ele)
#with index number
for x,y in np.ndenumerate(arr2):
    print(x,y)


#for 3D
for ele in np.nditer(arr3):
    print(ele)
#with index number
for x,y in np.ndenumerate(arr3):
    print(x,y)

