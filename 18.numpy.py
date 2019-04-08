import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import sys
sys.modules.keys()

import types
def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__


release = pd.read_csv('dataset\data\\release_dates.csv', index_col=None)
release.head()

titles = pd.read_csv('dataset\data\\titles.csv')
titles.head()

d = np.array([1, 2, 3, 4])
type(d)
d

nd = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
nd

nd[0][0]
nd.shape
df = pd.DataFrame(nd[0])
df
df = pd.DataFrame(nd[0][0])
df
nd.dtype
np.zeros(3)
np.zeros([3, 3])

# diagonal matrix
e = np.eye(3)

# add 1 to all elements
e2 = e + 1
e2

# create matrix with all entries as 1 and size as 'e2'

o = np.ones_like(e2)
o.dtype
o_int = o.astype(np.int32)
o_int


# convert string-list to float
a = ['1', '2', '3']
a
a_arr = np.array(a, dtype=np.string_)
a_arr
af = a_arr.astype(np.float)
af, af.dtype

data = np.random.randn(5, 3)
data

name = np.array(['a', 'b', 'c', 'a', 'b'])
name == 'a'

data[name=='a']
data[name != 'a']

