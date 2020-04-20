import numpy as np
import pandas as pd

# In broadcasting, we make use of NumPy's ability to combine arrays that don't have
# the same exact shape. Here is an example:

ar = np.arange(5)
ar


array_random = np.random.random_integers(1, 10, 10)
array_random

sorted_array = array_random.sort(axis=0)
sorted_array

np.sort(array_random)

ar=np.array([[3,2],
            [-1,10]])
ar[0]
ar[1]

ar.sort(axis=1)
ar
ar=np.array([[3,2],
            [-1,10]])
ar
ar.sort(axis=1)
ar

ar=np.array([[2,1],
            [12,10]])

ar.sort(axis=1)
ar