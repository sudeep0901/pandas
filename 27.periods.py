
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

rng = pd.date_range('2011-03-01', periods = 10, freq = 'M')
rng
type(rng)
rng[0]

rng1= pd.date_range(start= '2019-01-01', end = '2019-12-31', freq = '12H')
rng1

# Time zone can be specified for generating the series


rng = pd.date_range(start = '2015 Jul 2 10:15', end = '2015 July 12', freq = '12H', tz=
'Asia/Kolkata')
rng

rng.tz_convert('Australia/Sydney')

dd = ['07/07/2015', '08/12/2015', '12/04/2015']
# convert into date

list(pd.to_datetime(dd))

