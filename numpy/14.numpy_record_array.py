import numpy as np
import pandas as pd

person_record_array = np.rec.array([('Delta', 10, 29 , 29 ,34)])
person_record_array[0]

a = 2

a, b = 10, 20
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a") 