import numpy as np
import pandas as pd

person_data_def = [('sudeep','S8'), ('height', 'f8')]


person_array =  np.zeros((4), dtype = person_data_def)

person_array[0] = ('Sudeep', 180)

person_array[0][1]
name = person_array[0][0]
name

for val in person_array:
    person_array_1 =  np.zeros((4), dtype = person_data_def)
    print(val[0], val[1])

person_array_1


def add(a, b):
    a = 1
    b = 10
    print(a, b)
    print(id(a), id(b))
    print(add.__dict__)



a = 1
b =10

print(id(a), id(b))
print(a, b)

answer = add(a, b)
print(id(a), id(b))
print(a, b)
print(add.__dict__)


a =  b

print(id(a), id(b))

c= None
d = np.nan

print(id(c), id(d), type(None))


# numpy record array built on structured array
per_array  =np.rec.array([('Mansavi', 8)], dtype=person_data_def)

per_array[0].sudeep
per_array[0].height

import string
string.ascii_lowercase
string.ascii_uppercase
string.whitespace
string.digits
string.hexdigits
print("sudeep" + string.whitespace + "patel")