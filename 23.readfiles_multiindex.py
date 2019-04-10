import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

 df = pd.read_csv('ex_mulindex.csv', index_col=['key1','key2'])
 df
 df.index

 df.unstack()
 df.unstack(level='key2')
