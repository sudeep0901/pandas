import pandas as pd
import numpy as np


titles = pd.read_csv("dataset\data\\titles.csv", index_col=None)
titles.head()
t = titles

macbeth = t[ t['title'] == 'Macbeth']
macbeth

# by default index
macbeth = t[ t['title'] == 'Macbeth'].sort_index()
macbeth

macbeth = t[ t['title'] == 'Macbeth'].sort_values('year', ascending=False)
macbeth

t
suzon = t[ t['title'] == 'Suzanne']
suzon

casts = pd.read_csv("dataset\data\cast.csv", index_col=None)
casts.columns

casts.iloc[3:5]


df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
       index=['cobra', 'viper', 'sidewinder'],
       columns=['max_speed', 'shield'])

df
df.loc[['cobra', 'viper']]
df.loc['cobra':'viper', 'max_speed': 'shield']
df.loc[:,'shield']

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
