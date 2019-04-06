import pandas as pd
import numpy as np

data = { 'name' : ['AA', 'IBM', 'GOOG'],
'date' : ['2001-12-01', '2012-02-10', '2010-04-09'],
'shares' : [100, 30, 90],
'price' : [12.3, 10.3, 32.2]
}

df = pd.DataFrame(data)


data['owner'] = 'Unknown'
df['shares']

df.index.values
*range(1, 10)

del df['owner']
df

df.drop('shares', axis=1)


