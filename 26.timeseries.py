
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

 pr = pd.Period('2012', freq = 'M')
 pr

 pr.asfreq('D', 'start')
 pr.asfreq('D', 'end')

pr.asfreq('M', 'start')
pr.asfreq('M', 'end')

pr = pd.Period('2012', freq='A')
pr

pr + 1


pr = pr.asfreq('D')

pr = pr + 1
pr =pr.to_timestamp()

td = pd.Timedelta('3 M')

pr + td

df = pd.read_csv('dataset\data\\time\\stocks.csv')

df
df.columns

type(df.date[0])


df = pd.DataFrame.from_csv('dataset\data\\time\\stocks.csv', parse_dates=['date'])
df.date

df = pd.DataFrame.from_csv('dataset\data\\time\\stocks.csv', parse_dates=['date'], index_col='date')
df

del df['Unnamed: 0']

df.index.name

stocks = pd.DataFrame.from_csv('dataset\data\\time\\stocks.csv', parse_dates=['date'])
stocks.head()
stocks.index.name
stocks = stocks.set_index('date', drop = 'false')
stocks.index.name
