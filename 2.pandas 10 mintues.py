#%%
import numpy as np
import pandas as pd
sr = pd.Series([1, 3, 5, np.nan])
print(sr)


# pd.date_range
# generate 12 months index for an year
dates = pd.date_range('2011', periods=12)
print(dates)
dates = pd.date_range('20110101', periods=365,freq='D')
print(dates)

dates = pd.date_range('20190101', periods=12,freq='M')
print(dates)    

df = pd.DataFrame(np.random.randn(6, 4), 
index=pd.date_range('20190101', periods=6, freq='M'), columns=list('ABCD'))
print(df)

# create a dataframe using dictionary

df1 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E':pd.Categorical(['train','test', 'train', 'test']),
    'F': 'foo'
})

print(df1, df1.dtypes)
print(df1.index)
print(df1.columns)

# print(df1.to_numpy())
print("Describe:------------")
print(df.describe())
print("transpose Data:-----------------")
print(df.T)

print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=0, ascending=False))
print(df['A'], "\n")
print(df.iloc[3], df)
print(len(df)) # rows in data frame
print(len(df.columns)) # lent in data frame

df2 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df2)

# handle missing values
print(df2[df2['E'].isin([np.nan])])
df3 = df2.dropna(how='any')
print(df3)

print(pd.isna(df2))

#historgramming

s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
# s = s.reindex(index=s.value_counts())
print(s)