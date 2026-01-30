# Rounding Decimals
# There are primarily five ways of rounding off decimals in NumPy:

# truncation=will return near to zero value with float number
# fix=same as truncation
# rounding=The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# floor=nearest to lowest zero
# ceil=nearest to highest integer
import numpy as np

arr1=np.trunc([-3.123,3.166])
print(arr1)

arr2=np.fix([-3.123,3.166])
print(arr2)

arr3=np.around([-3.66,-3.122,3.66,3.122])
print(arr3)

arr4=np.floor([-3.66,-3.122,3.66,3.122])
print(arr4)

arr5=np.ceil([-3.66,-3.122,3.66,3.122])
print(arr5)
