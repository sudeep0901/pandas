import numpy as np
import pandas as pd

# In broadcasting, we make use of NumPy's ability to combine arrays that don't have
# the same exact shape. Here is an example:

ar = np.ones([3, 2]); ar

ar2 = np.array([2, 3]); ar2
ar+ar2