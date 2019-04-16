import numpy as np
import pandas as pd
# 1 dim array
ar1 = np.array([1, 2, 3, 4])
ar2 = np.array([[1, 2, 3, 4], 
               [6, 7, 8, 9],
               [6, 7, 8, 9],
               [6, 7, 8, 9]
               ])

pd.DataFrame(data=ar2)
ar2 
ar2[1][1:4]
ar2.shape
ar2.ndim

np.arange(1, 12, 1) # not inclusive 12

np.linspace(1, 10, 100)

np.ones((2, 3, 2))

np.zeros((2, 3, 4))

np.eye(3)

np.diag((1, 4, 5, 6))

np.random.seed(100)
np.random.rand(3)

np.random.randn(10)

np.empty((3, 3))

np.tile(np.array([['sudeep', 'patel'], [1, 3]]), (2, 2))

np.tile(np.array(np.arange(1, 4)), (3,3))