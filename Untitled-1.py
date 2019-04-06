
#%%
import pandas as pd
import numpy as np


#%%
d = {
    'col1': [1, 2],
    'col2': [3,4]
}

df = pd.DataFrame(data =d )
df


#%%
df.iloc[0]


#%%
df.loc[0]


#%%
df['col1']


#%%
df['col2']


#%%
df.dtypes


#%%
df = pd.DataFrame(data=d ,dtype=np.int8)


#%%
df.dtypes


#%%
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8 , 9 ]]), columns=['a', 'b', 'c'])


#%%
df2


#%%
df2.T # TRANSPOSED


#%%
import numpy as np


#%%
s = pd.Series([1, 3, 4, np.nan, 6, 8])


#%%
s


#%%
s.dtype


#%%
type([1])


#%%
dates = pd.date_range('010198', periods=12)


#%%
dates


#%%
df = pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list('ABCD'))


#%%
df


#%%
df = pd.DataFrame(np.random.randn(12, 12), index=dates, columns=list('123412341234'))


#%%
# df['2'] = 0


#%%
range(1, 10)


#%%
l =list(range(1, 10))


#%%
for n in range(1, 10):
    print(n)


#%%
l


#%%
indices  = [x for  i , x  in enumerate(l) if x > 2]
print(indices)


#%%
def add(a, b):
    print(a)
    print(id(a))
    res = a + b
    a = a + a
    print(id(a))
    b=200
    return res    


#%%
a, b = 2,3
print(id(a))
print(add(a, b))
print(a)


#%%
a


#%%
3


#%%
l.reverse()


#%%
print(l)


#%%
e = enumerate(l)


#%%
for index, item in enumerate(l):
    print(index, item)


#%%
def good_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)
    return a_list


#%%
good_append('one')


#%%
good_append('two')


#%%
nums = pd.DataFrame([range(1, 3)])


#%%
nums.shape


#%%
nums


#%%
df2 = pd.DataFrame({
    'A':1.,
    'B': pd.Timestamp('20190101'),
    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3]* 4, dtype='int32'),
    'E':pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})


#%%
df2
df2['E']


#%%
arr = np.array([3] * 10)


#%%
list(arr)


#%%
import string


#%%
string.ascii_uppercase[:-2]


#%%
s = np.array(["testing"] * 24)


#%%
l1 = list(zip(string.ascii_uppercase[:-2],list("testingtesting"), range(25)))
l1


#%%
df2.describe


#%%
df2.dtypes


#%%
df2.index


#%%
# l1[0][0] + l1[0][1] + string(l1[0][2])


#%%
df.index


#%%
for indx in enumerate(df.index):
    print(indx[0], indx[1], indx)


#%%
df.columns


#%%
df2.columns


#%%
df2.columns[0]


#%%
print(df2.describe())


#%%
df2


#%%
df2['B'].T


#%%
df2


#%%
df


#%%
df.sort_index(axis=1, ascending=False)


#%%
df.values


#%%
dates = pd.date_range('20130101', periods=6)
df3 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df3


#%%
df3.sort_index(axis=1, ascending=False) # sort index


#%%
df3.sort_index(axis=0, ascending=False) # sort index


#%%
df3.sort_values(by=['A','B'], ascending=False) # SORTY BY COLUMN values


#%%
df3['A']


#%%
v='sudeep' + string.whitespace + string.punctuation + string.hexdigits + string.octdigits
v


#%%
df3[0:3]


#%%
df3['20130102':'20130104']


#%%
df3.loc[dates[1]] # by index


#%%
df3.loc[dates[0]:dates[1],['A','B']]


#%%
df3.loc['20130101':'20130102',['A']]


#%%
df3.loc['20130102', ['A', 'B']]


#%%
df3.loc[dates[2], 'A'] # Scalar value


#%%
idx = df3.index


#%%
idx.values


#%%
L =df3.loc[idx[0]]
L.dtype


#%%
df3.at[dates[0], 'A']


#%%
df3.iloc[0:3]


#%%
df3.iloc[3:5, 0:2]


#%%
df3


#%%
df3.iloc[[1, 2, 4], [0, 2]]


#%%
df.iloc[1:3,:]


#%%
len(df3['A'])


#%%



#%%
df3.iloc[3:, :]


#%%
df3.iloc[3]


#%%
df3.iloc[1:3,:]


#%%
ll = df3.iloc[:, 1:3]
ll


#%%
df3.iat[1, 1]


#%%
BL = [df3.A > 1]
BL


#%%
df3['A']


#%%
df3['NEWCOL'] = ['one', '2', '3', '4', '5', '6']


#%%
df3


#%%



#%%
df3[df3['NEWCOL'].isin(['2'])]


#%%
s1 =  pd.Series(range(10,70,10), index=pd.date_range('20130102', periods=6))


#%%
s1


#%%
df3['G']=s1


#%%
df3


#%%
table2 =list(range(1, 11))
table2


#%%
seq2=[2] * 10
seq2


#%%



#%%
[x * 2 for x in table2 ]


#%%



#%%
len(np.array([2] * 10))
seq2 = np.array([2] * 10)
seq2
seq2=np.transpose(seq2)
seq2


#%%
data = pd.DataFrame([ table2, [x * 2 for x in table2 ]])
data.T


#%%
import numpy as np
import pandas as pd
x = np.random.randn(5)
y = np.sin(x)
df = pd.DataFrame({'x':x, 'y':y})
df.plot('x', 'y', kind='scatter')


#%%
data = np.array( [[2]*10, table2, [x * 2 for x in table2]])
data


#%%
pd.DataFrame(data=data, columns='A', 'B', 'C')


#%%
data= data.T
data
data[1]


#%%
d = {
    'A': range(1,11),
    'B': [2] * 10, 
    'C': [x * 2 for x in range(1, 11)]
}

df = pd.DataFrame(data =d )
df


#%%
df.A


#%%



#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm


#%%
from sklearn.model_selection import train_test_split
X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])


#%%
X[1][0]
y = [0,1,0,1,0,1]


#%%
clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)
 


#%%
print(clf.predict([[1,2]]))


#%%
print(clf.predict([[10.58,10.76]]))


#%%
X


#%%
X = np.array([[2,1,1],
             [2,2,1],
             [2,3,1 ],
             [2,4, 1],
             [2,5,1],
             [2,6,1],
             [2,7,1],
             [2,8,1],
             [2,9, 1],
             [2,10,1]])


#%%
y =  [2, 4, 6, 8, 10, 12,14,16,18,20]


#%%
clf.fit(X,y)


#%%
clf.predict(X)


#%%
w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()


#%%
w = clf.coef_[0]


#%%
w


#%%
X = ["SUDEEP", 'manasvi', "rajesh"]
X


#%%
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()


#%%
X_train_counts = count_vect.fit_transform(X)
X_train_counts.shape


#%%
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape
target =['Ratlam','indore', 'ujjain']


#%%
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf,target )


#%%
import numpy as np
twenty_test = [['sudeep']]
predicted = clf.predict(twenty_test)
# np.mean(predicted == target)


#%%



