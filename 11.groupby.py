import matplotlib.pyplot as plt
import pandas as pd
titles = pd.read_csv("dataset\data\\titles.csv", index_col=None)
titles.head()
t = titles

casts = pd.read_csv("dataset\data\cast.csv", index_col=None)
casts.columns

cg = titles.groupby(['year']).size()
cg

cg.plot()
plt.show()

# group by actor films

c = casts
c.groupby(['year', 'name']).size()
cf = c[c['name'] == 'Aaron Abrams']
cf.groupby(['year']).size().plot()

c.groupby(['year', 'name']).n.max().plot()
c.groupby(['year']).n.mean().head()

decade = c['year']//10*10
decade
c_dec = c.groupby(decade).n.size()
c_dec.plot()