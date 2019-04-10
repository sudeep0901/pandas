import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame.from_csv('ex1.csv', index_col=None)
df.index

df=pd.read_csv('ex1.csv')
df

df = pd.read_table('ex1.csv', sep=',')
df
type(df)

df_no_header = pd.read_table('ex1.csv', sep=',', header=None)
df_no_header
df.index

df_no_header = pd.read_table('ex1.csv', sep=',', names=['header1', 'header2', 'header3', 'header4'])

df_no_header
df_no_header = pd.read_table('ex1.csv', sep=',', index_col=['message', 'a'])
df_no_header
df_no_header.stack().unstack()
