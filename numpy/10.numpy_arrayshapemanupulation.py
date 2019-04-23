import numpy as np
import pandas as pd

# In broadcasting, we make use of NumPy's ability to combine arrays that don't have
# the same exact shape. Here is an example:

 # flattening the multidimentional array 

 ar = np.array([[[1, 2, 3,],
                [1, 2, 3,],
                [1, 2, 3,]]])

ar

%timeit ar.ravel().astype(str)
%timeit ar.ravel().astype(float)
%timeit ar.ravel().astype(int)

# np.ravel returns view
ar2 = np.array([np.arange(1, 6), np.arange(10, 15)])
ar2

ar_view = ar2.ravel()
ar_view
ar_view[0] =100
ar2[0][0] =200
ar_view

ar_view
ar_view = ar2.T.ravel() # by columns wise

ar.T.ravel()


# .flatten return copy of array
ar2.flatten()




# reshape()


re_array = np.arange(0, 16); re_array
re_array.reshape(4, 4)
re_array.reshape(2, 8)
re_array.reshape(8, 2)
re_array.reshape(1, 16)

# return view of data
re_array.reshape(2, 2, 4).shape


