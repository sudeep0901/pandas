import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


release = pd.read_csv('dataset\data\\release_dates.csv', index_col=None)
release.head()

cast = pd.read_csv('dataset\data\\cast.csv', index_col=None)
cast.head()

 cm = cast.set_index(['title', 'n']).sort_index()
 cm.stack()
 cm.index[1][0]
 cm.index[1][1]

cm.loc['#DigitalLivesMatter']

cm.loc[cm.index[1][0]]
cm.loc['Macbeth']

cm.loc['Macbeth'].loc[4:18]
cm.loc['Macbeth'].loc[4]

# remove index
cm.reset_index('n')
cm.index.value_counts()[0]
cm.loc[cm.index[0]]
