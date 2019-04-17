import numpy as np
import pandas as pd



# Array masking

# np.random.seed(10)

ar = np.random.random_integers(0, 25,10)

ar

evenMask = (ar % 2 == 0)
evenMask

ar[evenMask]

# seed(0) let's generate same sequence of random numbers in each iteration
np.random.seed(0)
np.random.rand(4)
