import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4])

print(s.interpolate())
s = pd.Series([1, 2, np.nan,np.nan , 10])

print(s.interpolate())      

s = pd.Series(['a', 'sudeep', np.nan, 'filling_more', np.nan, 'Bharat'])
print(s.interpolate(method='pad'))

s = pd.Series([0, 2, np.nan, 8])

print(s.interpolate(method='polynomial', order=2))

