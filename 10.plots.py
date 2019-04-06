import matplotlib.pyplot as plt
import pandas as pd
titles = pd.read_csv("dataset\data\\titles.csv", index_col=None)
titles.head()
t = titles

casts = pd.read_csv("dataset\data\cast.csv", index_col=None)
casts.columns

t = titles
t

p = t['year'].value_counts()
p.sort_index(ascending=False).plot()
p.plot()
plt.show()
t.columns

p = t['title'].value_counts()
p.sort_index().plot()
p.plot()
plt.show()

