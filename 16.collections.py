import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

release = pd.read_csv('dataset\data\\release_dates.csv', index_col=None)
release.head()

titles = pd.read_csv('dataset\data\\titles.csv')
titles.head()

from collections import defaultdict

d = defaultdict(list)
titles
for row in titles:
    # d[row['year']].append(row['title'])
    print(row)

    
xx=[]
yy=[]

for k, v in d.items():
    xx.append(k)# = k
    yy.append(len(v))# = len(v)
    plt.plot(sorted(xx), yy)
    plt.show()