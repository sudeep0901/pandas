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

print("Size of data aftger group by:--------------")
print(cf.groupby(['year']).size())
c.groupby(['year', 'name']).n.max().plot()
c.groupby(['year']).n.mean().head()

# 2.3.2 Groupby with custom field
decade = c['year']//10*10
decade
c_dec = c.groupby(decade).n.size()
c_dec.plot()



c_decade = c.groupby( ['type', c['year']//10*10] ).size()
c_decade.unstack()

c_decade.unstack().plot()
plt.show()

c_decade.unstack().plot(kind='bar')
plt.show()

# to plot side by side

c_decade.unstack(0)

c_decade.unstack(0).plot(kind='bar')
plt.show()


print("Size:", titles.size)
print("shape:", titles.shape)
print("ndim:", titles.ndim)

stk = casts.stack()
stk.unstack()

    