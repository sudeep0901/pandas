import numpy as np
import pandas as pd


array = np.array((np.random.rand(10) * 100).astype(int))
array

# reverse an array  double colon 
array[::-1]

array[::3]

# array(startIndex : endIndex: stepValue)
array[0:4:4]

array[0,3:4]

a = np.reshape(np.arange(9),(3,3))
a
a[0,3:]

x = np.array([
     [[1],[2],[3]],
     [[4],[5],[6]]
    ])
x
x.ndim


x[...,0]
x[0,...]
x[1,...]
x[-1,...]

x
x[:,np.newaxis,:,:]



x[:,0: 4]

dim_3_arry = np.array(
    [
        [
         [1, 21, 3], 
         [4, 5, 6], 
         [7, 8, 9]
        ],

        [
            [19, 22, 33], 
            [44, 5, 6], 
            [7, 8, 9]],

        [
            [11, 23, 30], 
            [4, 5, 6], 
            [7, 8, 99]
        ]
    ])


dim_3_arry.shape
dim_3_arry
dim_3_arry[[0], [0],[0]]
dim_3_arry[[0], [0],[1]]
dim_3_arry[[0], [0],[2]]

dim_3_arry[[0, 1]]
dim_3_arry[[0, 1], [0],[2]]


dim_3_arry[[0, 1, 2], [0, 1, 0]]


dim_3_arry[[0, 1, 2], [0, 1, 2]]

dim_3_arry[[1, 1], [2, 1]]

np.arange(0, 16)
by_4_4 = np.arange(1, 17).reshape(4,4)

rows = np.array([[0, 0 ], [3, 3]],  dtype=np.intp)
columns = np.array([[0, 2], [0, 2]], dtype=np.intp)
rows
columns


by_4_4
by_4_4[1:3,1:3]
by_4_4[1:3,[1,2]]

dim_3_arry

dim_3_arry[::-1,:,:]
dim_3_arry[1,1,1]

dim_3_arry
found = np.where(dim_3_arry == 99)
type([found])
found = [found]
len(found)
found[0][1]

