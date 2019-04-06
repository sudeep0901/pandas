import pandas as pd
import numpy as np

data = {
    'name': ["sudeep","Brajesh", "rajesh"],
    'age': [33, 35, 34], 
    'dob': pd.date_range('2019',periods=3),
    'salary': ['100k', '200k', '101k']
}

print(data)

df = pd.DataFrame(data)
print(df)

print(df['name'] )

df['remarks'] = 'None'
print(df)

print(df.index)
print(np.arange(10, 40, 10))
df.index = np.arange(10, 40, 10)
df.index = df.index * 10
print(df.index)

# setting up column as index
df  = df.set_index(['name'])
print(df.ix['sudeep'])