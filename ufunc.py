# ufunc means universal functions
# it is used to implement vectoraization in numpy.
# Converting iterative statements into a vector based operation is called vectorization.

# o create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

import numpy as np

def add(a,b):
    return (a+b)

my_add=np.frompyfunc(add,2,1)

print(add([10,20],[30,40]))
