import numpy as np
import pandas as pd

# In broadcasting, we make use of NumPy's ability to combine arrays that don't have
# the same exact shape. Here is an example:

ar = np.arange(5)
ar
# resizing
ar.resize((8,))
ar
ar.resize((8))
ar

ar2 = ar



# ValueError: cannot resize an array that references or is referenced
# by another array in this way.
# Use the np.resize function or refcheck=False
ar.resize((8,))
np.resize(ar, (80,))
ar_resized = np.resize(ar, (8,))
ar_resized

ar_resized

ar_newaxis=np.array([14,15,16]); ar.shape

ar_newaxis1 =ar[:,np.newaxis]
ar_newaxis1
ar_newaxis1.shape
ar_newaxis2 =  ar_newaxis1[:,np.newaxis]
ar_newaxis2
ar_newaxis2.shape


mul_array = np.array([[[1,1, 1],
                [2,2,2]]])

type(mul_array)
mul_array

mul_array.shape
mul_array
mul_array[np.newaxis, : ]




