import numpy as np
import pandas as pd

# combining larger array in smaller array

ar = np.arange(15)
ar 

ar2 = np.arange(0, -10, -1)[::-1]
ar2 

ar[:10] = ar2
ar