import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

release = pd.read_csv('dataset\data\\release_dates.csv', index_col=None)
release.head()

cast = pd.read_csv('dataset\data\\cast.csv', index_col=None)
cast.head()

import csv

titles = list(csv.DictReader(open('dataset\data\\titles.csv')))
titles[0:5]
titles.index

for k, v in titles[0].items():
    print(k, ':', v)

def readValus(row):
    for k, v in row[0].items():
        print(k, ':', v)

year85 =  [a for a in titles if a['year']=='1985']
year85[:5]

# movies from 1990 to 1999
movies90 = [m for m in titles if (int(m['year']) < int('2000')) and (int(m['year']) > int('1989'))]
movies90[:5]

# movies from 1990 to 1999
movies90 = [m for m in titles if (int(m['year']) < int('2000')) and (int(m['year']) > int('1989'))]
movies90[:5]


# find Macbeth movies
macbeth = [m for m in titles if m['title']=='Macbeth']
macbeth[:3]

from operator import itemgetter
sorted(macbeth, key=itemgetter('year'))

casts = list(csv.DictReader(open('dataset\\data\cast.csv')))
casts[3:6]

# replace '' with 0
cast0 = [ c for c in casts]
cast0

cast0 = [{**c, 'n':c['n'].replace('', '0')} for c in casts]
cast0[3:5]

cast0 = [c['n'].replace('', '0') for c in casts]
cast0[3:5]

# Movies starts with Maa
maa = [m for m in titles if m['title'].startswith('Maa')]
maa[:3]

