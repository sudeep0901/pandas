
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.DataFrame({ 'key' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
'data1' : range(7)})

df1
df1.loc[1]


df2 = pd.DataFrame({ 'key' : ['a', 'b', 'd'],
 'data2' : range(3)})

df2

df3 = pd.merge(df1, df2)
df3

df3 = pd.merge(df1, df2, on='key')
df3


df4 = pd.DataFrame({ 'key1' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
 'data1' : range(7)})

df4 
df5

df5 = pd.DataFrame({ 'key2' : ['a', 'b', 'd', 'b'],
 'data1' : range(4)})

pd.merge(df4, df5, left_on='key1',right_on='key2')

# left join
df6 = pd.merge(df4, df5, left_on='key1', right_on='key2', how="left")
pd.isnull(df6)

df6

df7 = pd.merge(df4, df5, left_on='key1', right_on='key2', how="right")
pd.isnull(df7)

df8 = pd.merge(df4, df5, left_on='key1', right_on='key2', how="outer")
pd.isnull(df8)