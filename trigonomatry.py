import numpy as np

arr1=np.array([np.pi/2,np.pi/4,np.pi])
arr2=np.sin(arr1)
print(arr2)

arr3=np.cos(arr1)
print(arr3)

arr4=np.tan(arr1)
print(arr4)

#digree to redian and redian to digree

arr5=np.array([np.pi/2,np.pi/4,np.pi])
arr6=np.rad2deg(arr5)
print(arr6)

arr7=np.array([30,45,60,90,120])
arr8=np.deg2rad(arr7)
print(arr8)

#finding angles

arr9=np.array([0,-1,1])
arr10=np.arcsin(arr9)
print(arr10)

arr11=np.arccos(arr9)
print(arr11)


#finding hypotanous
base=10
perp=20
hyp=np.hypot(base,perp)
print(hyp)