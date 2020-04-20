import pandas as pd
import numpy as np
# ser = pd.Series(data, index=idx)
# keys becomes index
np.random.seed(0)
ser = pd.Series(np.random.rand(5)); ser

import calendar as cal
print(cal.month_abbr)
# monthnames
monthnames = cal.month_abbr
print(monthnames)
months = pd.Series(np.arange(1, 14), index=monthnames)
months
months.index
months['January']


currDict = {

    "US": "Dollar", 
    "UK": "Pound",
    "Bharat": "Rupee"
}

print(currDict)

ser = pd.Series(currDict)
print(ser)
print(ser.index)
print(ser.values)

[print(val) for val in ser.values]
values = [print(val) for val in ser.index]
values
stockPrices = {'GOOG':1180.97,'FB':62.57,
'TWTR': 64.50, 'AMZN':358.69,
'AAPL':500.6}

stockPriceSeries=pd.Series(stockPrices,
index=['GOOG','FB','YHOO',
'TWTR','AMZN','AAPL'],
name='stockPrices')

stockPriceSeries
stockPriceSeries

dogSeries = pd.Series('dobberman')
dogSeries
type(dogSeries)
dogSeries = pd.Series('dobberman',
            index=['A', 'B','C'])
dogSeries

const = pd.Series("Non Available", index=np.arange(1, 1001))
dogSeries.T

pd.Series(const.index, index = const.values)


stockPrices

# key error
# stockPrices['MSFT']

stockPrices.get('MSFT', np.nan)
stockPrices

stockPriceSeries
stockPriceSeries[:4]
# 2 is step
stockPriceSeries[::2]

np.std(stockPriceSeries)
stockPriceSeries[2:]

stockPriceSeries[:-2]
stockPriceSeries
stockPriceSeries[2:] + stockPriceSeries[:-2]


# For scalar data, an index must be provided. The value will be repeated for as many
# index values as possible. One possible use of this method is to provide a quick and
# dirty method of initialization, with the Series structure to be filled in later. Let us see
# how to create a Series using scalar values:

