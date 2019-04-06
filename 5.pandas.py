import pandas as pd
import numpy as np

# convert tuple in Series

# tp = tuple(1, 2, 3)
# print(tp)

h = ('AA', '2012-02-01', 100, 10.2)
s = pd.Series(h)
# print(s)

data = {
    'name':['AA', 'CC', 'BB'],
    'date': pd.date_range('2019', periods=3),
    'shares' : [100, 30, 90],
    'price': [12.3, 10.3, 32.2]
}


df = pd.DataFrame(data)
print(df)


# converting dict to tuple

dict = {    "name":'sudeep', "last": ["Patel","Mahesh"]}

ds = pd.Series(dict)
print(ds)
print( ds[0])
print(ds['name'] + ds['last'])

inxArr = ['name','last']

print(ds[inxArr])

ser = pd.Series([1, 2, 3, 4])
fruits = ['lemon', 'pear', 'watermelon', 'tomato']

print(*range(1,10))

