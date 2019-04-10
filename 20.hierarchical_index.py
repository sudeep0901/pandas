import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.Series([10, 20, 30, 40, 15, 25, 35, 25], index = [['a', 'a',
  'a', 'a', 'b', 'b', 'b', 'b'], ['obj1', 'obj2', 'obj3', 'obj4', 'obj1',
  'obj2', 'obj3', 'obj4']])

data


data1 = pd.Series([1, 2, 3,4] , index = [
    ['a', 'a', 'b', 'b'], ['o1', 'o2', 'o3', 'o4']
])

data.index

# Choosing a particular index from a hierarchical indexing is known as partial indexing.

data['a','obj1']
data[:, 'obj2']

data['a','obj2']
data.unstack()

data2 = pd.DataFrame({'a': [ 1,2, 3, 4],
'b': [ 5,62, 73, 84]
})

data2_stack = data2.stack()
data2_stack
data2_stack[0]
data2_stack[0,'a']
(data2.stack()).unstack(0) # Level 0
(data2.stack()).unstack(1) # Level 1


# column indexing
df = pd.DataFrame(np.arange(12).reshape(4, 3),
index = [['a', 'a', 'b', 'b'], ['one', 'two', 'three', 'four']],
columns = [['num1', 'num2', 'num3'], ['red', 'green', 'red'], ['red', 'green', 'red']]
)

df

df.index
df.columns  
df['num1']
df['num1', 'red','red']
df['num2']

df.index.names=['key1', 'key2']
df.columns.names=['n', 'color']
df
df.swaplevel('key1', 'key2')
df.sort_index(level='key1')
df.sort_index(level='key2')
df.sum(level='key1')
