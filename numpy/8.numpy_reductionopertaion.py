import numpy as np
import pandas as pd

#  Basic operations

ar = np.arange(1, 5)
ar

ar.prod()

ar.sum()
ar.cumsum()
ar.mean()
np.median(ar)

ar
ret = np.any((ar < 5))

ret