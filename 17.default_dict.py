import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

release = pd.read_csv('dataset\data\\release_dates.csv', index_col=None)
release.head()

titles = pd.read_csv('dataset\data\\titles.csv')
titles.head()

titles['year']


cast = pd.read_csv('dataset\data\\cast.csv', index_col=None)
cast.head()

from collections import Counter

by_year = Counter(t['year'] for t in titles)
by_year