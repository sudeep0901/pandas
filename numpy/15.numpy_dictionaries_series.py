import numpy as np
import pandas as pd

stockSummaries={
'AMZN': pd.Series([346.15,0.59,459,0.52,589.8,158.88],
index=['Closing price','EPS',
'Shares Outstanding(M)',
'Beta', 'P/E','Market Cap(B)']),
'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
index=['Closing price','EPS','Shares Outstanding(M)',
'Beta','P/E','Market Cap(B)']),
'FB': pd.Series([61.48,0.59,2450,104.93,150.92],
index=['Closing price','EPS','Shares Outstanding(M)',
'P/E', 'Market Cap(B)']),
'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
index=['Closing price','EPS','Shares Outstanding(M)',
'P/E','Beta', 'Market Cap(B)']),
'TWTR':pd.Series([65.25,-0.3,555.2,36.23],
index=['Closing price','EPS','Shares Outstanding(M)',
'Market Cap(B)']),
'AAPL':pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
index=['Closing price','EPS','Shares Outstanding(M)','P/E',
'Market Cap(B)','Beta'])}


stockSummaries['AMZN']

stockDF = pd.DataFrame(data=stockSummaries)
stockDF.T
stockDF


dict = {
    "Cities":  pd.Series(["Indore", "ratlam", "mumbai", "delhi"]),
    "Cities1":  pd.Series(["Indore", "ratlam", "mumbai", "delhi"]),
    "Cities2":  pd.Series(["Indore", "ratlam", "mumbai", "delhi"]),
    "Cities3":  pd.Series(["Indore", "ratlam", "mumbai", "delhi"]),
    "Cities4":  pd.Series(["Indore", "ratlam", "mumbai", "delhi"])
}

dict

df = pd.DataFrame(dict)
df

len(dict)
df = pd.DataFrame(dict, columns= ['Cities1'])
df


