# A view on a NumPy array is just a particular way of portraying the data it contains.
# Creating a view does not result in a new copy of the array, rather the data it contains
# may be arranged in a specific order, or only certain data rows may be shown. Thus,
# if data is replaced on the underlying array's data, this will be reflected in the view
# whenever the data is accessed via indexing.

import numpy as np
import pandas as pd

# combining larger array in smaller array

np.may_share_memory

ar = np.arange(15)
ar 

ar2 = np.arange(0, -10, -1)[::-1]
ar2 

ar[:10] = ar2
ar

np.may_share_memory(ar, ar2)