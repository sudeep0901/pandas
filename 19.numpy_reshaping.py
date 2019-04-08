import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

a = np.arange(0, 16 )
a

a45 = a.reshape(2, 4)
a45 = a45.reshape(2,8)
a45.T


arr = np.arange(12).reshape(3,4)
arr
rn = np.random.randn(3, 4)
rn

rn1 = np.random.randn(3, 1)
rn1

# cocatene by row wise
# axis = 0 append  operation to existing array by row wise
np.concatenate([arr, rn], axis=0)

# append column wise error dimention of all the arrya must be same
np.concatenate([arr, rn, rn1], axis=0)

rn1.reshape(3, 4)

