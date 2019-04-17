import numpy as np
import pandas as pd


# views
ar1 = np.arange(12)
ar1

ar2 = ar1[::2]
ar2

ar2[1] = -100
ar1

# to force np to copy the data use copy funciton

ar = np.arange(8); ar
arc =  ar[:3].copy(); arc

np.may_share_memory(ar1, ar2)
np.may_share_memory(ar, arc)

