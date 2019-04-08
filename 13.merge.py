import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


release = pd.read_csv('dataset\data\\release_dates.csv', index_col=None)
release.head()

casts = pd.read_csv('dataset\data\\cast.csv', index_col=None)
casts.head()

c_amelia = casts[casts['title'] == 'Amelia']
c_amelia

rls = release[release['title'] == 'Amelia'].head()
c_amelia.merge(rls).head()


c = casts[ casts['name']=='Aaron Abrams' ]
c

c_costar = c.merge(casts, on=['title', 'year']).head()
c_costar

c_costar = c_costar[c_costar['name_y'] != 'Aaron Abrams']
c_costar