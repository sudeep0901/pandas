import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

index = pd.Index([3, 1, 2, 3, 4, np.nan])

print(index)

# nan values not counted
print(index.value_counts())

# With normalize set to True, returns the relative frequency by dividing all values by the sum of values.

index.value_counts(normalize=True)

index.value_counts(bins=3)

index.value_counts(dropna = True)

index.isnull()

index = index[index.isnull()].fillna('NA')

index
