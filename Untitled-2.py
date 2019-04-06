
#%%
# Introduction to Data structures
import pandas as pd


#%%
import numpy as np


#%%
s = pd.Series(np.random.randn(5), index = ['a', 'b','c','d', 'e'])


#%%
s
print(s.index)


#%%
s =  pd.Series(np.random.rand(5))


#%%
s


#%%
s = np.arange(5)
s


#%%
s = np.arange(5.)
s


#%%
s = np.arange(3, 7)
s


#%%
s = np.arange(10,20, 3)
s


#%%
s = pd.Series(np.arange(1,11), index=np.arange(10, 110, 10))
s


#%%
type(s)


#%%
grid =np.mgrid[0:5, 0:5]
grid
print(grid[0])
print(type(grid))


#%%
ogrid = np.ogrid[0:5, 0:5]
ogrid


#%%
ogrid[0]


#%%
ogrid[1]


#%%
linespace = np.linspace(0, 10,num=5)
linespace


#%%
linespace = np.linspace(1, 10, num=4)
linespace


#%%
zer = np.zeros(10)
zer


#%%
import matplotlib.pyplot as plt
N = 8
y = np.zeros(N)
x1 =  np.linspace(0,10, N, endpoint=False)
x2 = np.linspace(0,10, N, endpoint=True)


#%%
plt.plot(x1,y, 'o')
plt.plot(x2,y + 0.5, 'o')
plt.ylim(-0.1, 1)
plt.show()


#%%
s  = pd.Series(np.linspace(0,10, 6))
s


#%%
grid = np.mgrid[0:2, 0:2]
grid.shape


#%%
grid
print(grid[0])
print(grid[0][1])
print(grid[0][1][1])


#%%
s = pd.Series(np.arange(0,11, 10))
s


#%%
s = pd.Series(np.linspace(0,10, 5))
s


#%%
data =pd.DataFrame(data=s, index=['a'])
data


#%%
# FROM dICT
dict = {
    'b': 2, 
    'c': 44,
    'a':99
}
sr = pd.Series(data=dict)
sr


#%%
pd.Series(dict, index = ['b', 'a', 'c', 'd', 'e'])


#%%
pd.Series(np.arange(1,5), index=['b', 'a', 'c', 'd'])


#%%
scalar = pd.Series('sudeep', index=['a', 'b', 'c', 'e','f'])
scalar


#%%
s[1]


#%%
s[s < s.std()]


#%%
s[:3]


#%%
s[[1,2,3]]


#%%
np.log(s)


#%%
np.sqrt(s)


#%%
np.square(s)


#%%



