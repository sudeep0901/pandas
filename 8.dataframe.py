import pandas as pd
import numpy as np


casts = pd.read_csv("dataset\data\cast.csv")
casts


# no index will be created

casts = pd.read_csv("dataset\data\cast.csv", index_col=None)
casts.columns

titles = pd.read_csv("dataset\data\\titles.csv", index_col=None)
titles.head()


# set option to limit numer of rows and colums
pd.set_option('max_rows', 10 , 'max_columns', 10)
titles

# number of rows in df
len(titles)

t = titles['title']
t.iloc[0]
titles
titles.iloc[0]
titles.columns
titles['title']

# filtering data

after85 =  titles[titles['year'] > 2018]
after85
titles['year'] > 1985

t = titles
movies90 = t[ (t['year']>=1990) & (t['year']<2000) ]
movies90