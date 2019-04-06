import pandas as pd
import numpy as np

titles = pd.read_csv("dataset\data\\titles.csv", index_col=None)
titles.head()
t = titles

casts = pd.read_csv("dataset\data\cast.csv", index_col=None)
casts.columns

casts.iloc[3:5]

c = casts
c['n'].isnull().head()

c[c['n'] != c['n'].isnull()]
c[c['n'].notnull()]

# fillna
c[c['n'].isnull()].fillna('NA')
t = titles
t[t['title'] == 'Maa']

#str.startwith
t[t['title'].str.startswith("Su")].head(3)

t['year'].value_counts()
