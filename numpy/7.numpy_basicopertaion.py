import numpy as np
import pandas as pd

#  Basic operations
ar  = np.arange(1, 10)  * 5
ar
ar1 = np.arange(1, 10)  ** 2
ar1
# ar * 0.5

element_wise = 3  + np.arange(1, 10)
element_wise


ar / ar1
ar + ar1
%timeit 
ar - ar1

# for matrix multiplication use (.) operator
ar=np.array([[1,1],[1,1]])
ar2=np.array([[2,2],[2,2]])

ar.dot(ar2)

ar < ar2

np.logical_and(ar< ar2 , ar2 != ar)

np.pi
np.pi * 2 * 5

np.sin([np.pi, np.pi/2])

np.transpose(ar)

ar.T

val1 = np.arange(1, 5)
val2 = [1, 2, 3, 4]

# if every element is matched then return single true and not boolean array
np.array_equal(val1, val2)
np.all(val1 ==val2)
