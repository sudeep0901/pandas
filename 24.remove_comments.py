import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

 df = pd.read_csv('ex4.csv', skiprows=[0,2,3])
 df
 df.index

df.to_csv('d_out.csv')
df.to_csv('d_out2.csv', header=False, index=False)