import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), 
index= list('acefh'),columns=['one','two','three'])

df['four'] ='bar'
print(df)
df['five'] = df['one'] > 0
print(df)

df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df2)

navalues = pd.isna(df2)
print(navalues)
print(pd.isna(df2['one']))
print(pd.notna(df2['four']))

print(None == None, np.nan == np.nan)
print(type(np.nan))

# NAN is float

int_series = pd.Series([1, 2, 3, np.nan, 8])
print(type(int_series))

#int 
# int_series = pd.Series([1, 2, np.nan, 4], dtype='Int64')
# print(type(int_series))

# df2 = df2.fillna(value = 0)
# print(df2)

df3 =  df.copy()

df3['timestamp'] = pd.Timestamp('20190101') 
df3.loc[['a', 'c', 'h'], ['one', 'timestamp']] = np.nan
print(df3)

print(df3.get_dtype_counts())
# print(df3.value_counts)

print(df3.mean())
print(df3.cumsum(skipna=False))

print(df3.groupby('five'))

print("Df---------------------", df2)
df4 = df2.copy()
print("printing first element",df4.at['b', 'one'])
df4.at['b', 'one'] = 10
print(df4)
# df4['a', 0] = 11
df4 = df4.dropna()
print("df4-------------",df4)
