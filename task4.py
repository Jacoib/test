In [1]:

import pandas as pd
import numpy as np

In [2]:
from pandas import Series,DataFrame

In [3]:
obj = pd.Series([4,7,-5,3])
obj

Out[3]:
0    4
1    7
2   -5
3    3
dtype: int64

In [4]:
obj.values

Out[4]:
array([ 4,  7, -5,  3], dtype=int64)

In [5]:
obj.index

Out[5]:
RangeIndex(start=0, stop=4, step=1)

In [6]:
obj2 = pd.Series([4,7,-5,3],index=['d','b','a','c'])
obj2

Out[6]:
d    4
b    7
a   -5
c    3
dtype: int64

In [7]:
obj2.index

Out[7]:
Index(['d', 'b', 'a', 'c'], dtype='object')

In [8]:
obj2['a']

Out[8]:
-5
In [9]:
obj2['d'] = 6
obj2[['c','a','d']]

Out[9]:
c    3
a   -5
d    6
dtype: int64

In [10]:
obj2[obj2>0]


Out[10]:

d    6
b    7
c    3
dtype: int64
In [11]:
obj2 * 2
Out[11]:
d    12
b    14
a   -10
c     6
dtype: int64

In [12]:
np.exp(obj2)

Out[12]:
d     403.428793
b    1096.633158
a       0.006738
c      20.085537
dtype: float64


In [13]:

'b' in obj2


Out[13]:
True

In [14]:
'e' in obj2


Out[14]:

False
In [15]:
sdata = {'ohio':35000,'texas':71000,'oregon':16000,'utah':5000}
obj3 = pd.Series(sdata)
obj3
Out[15]:
ohio      35000
texas     71000
oregon    16000
utah       5000
dtype: int64
In [16]:
states = {'california','ohio','oregon','texas'}
obj4 = pd.Series(sdata,index=states)
obj4
Out[16]:
ohio          35000.0
texas         71000.0
oregon        16000.0
california        NaN
dtype: float64
In [17]:
pd.isnull(obj4)
Out[17]:
ohio          False
texas         False
oregon        False
california     True
dtype: bool
In [18]:
pd.notnull(obj4)
Out[18]:
ohio           True
texas          True
oregon         True
california    False
dtype: bool
In [19]:
obj4.isnull()
Out[19]:
ohio          False
texas         False
oregon        False
california     True
dtype: bool
In [20]:
obj3
Out[20]:
ohio      35000
texas     71000
oregon    16000
utah       5000
dtype: int64
In [21]:
obj4
Out[21]:
ohio          35000.0
texas         71000.0
oregon        16000.0
california        NaN
dtype: float64
In [22]:
obj3 + obj4
Out[22]:
california         NaN
ohio           70000.0
oregon         32000.0
texas         142000.0
utah               NaN
dtype: float64
In [23]:
obj4.name = 'population'
obj4.index.name = 'state'
obj4
Out[23]:
state
ohio          35000.0
texas         71000.0
oregon        16000.0
california        NaN
Name: population, dtype: float64
In [24]:
obj
Out[24]:
0    4
1    7
2   -5
3    3
dtype: int64
In [25]:
obj.index = ['bob','steve','jeff','ryan']
obj
Out[25]:
bob      4
steve    7
jeff    -5
ryan     3
dtype: int64
In [26]:
data = {'state':['ohio','ohio','ohio','nevada','nevada','nevada'],
       'year':[2000,2001,2002,2001,2002,2003],
       'pop':[1.2,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
frame
Out[26]:
state	year	pop
0	ohio	2000	1.2
1	ohio	2001	1.7
2	ohio	2002	3.6
3	nevada	2001	2.4
4	nevada	2002	2.9
5	nevada	2003	3.2
In [27]:
frame.head()
Out[27]:
state	year	pop
0	ohio	2000	1.2
1	ohio	2001	1.7
2	ohio	2002	3.6
3	nevada	2001	2.4
4	nevada	2002	2.9
In [28]:
pd.DataFrame(data,columns=['year','state','pop'])
Out[28]:
year	state	pop
0	2000	ohio	1.2
1	2001	ohio	1.7
2	2002	ohio	3.6
3	2001	nevada	2.4
4	2002	nevada	2.9
5	2003	nevada	3.2
In [29]:
frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],
                     index=['one','two','three','four',
                           'five','six'])
frame2
Out[29]:
year	state	pop	debt
one	2000	ohio	1.2	NaN
two	2001	ohio	1.7	NaN
three	2002	ohio	3.6	NaN
four	2001	nevada	2.4	NaN
five	2002	nevada	2.9	NaN
six	2003	nevada	3.2	NaN
In [30]:
frame2['state']
Out[30]:
one        ohio
two        ohio
three      ohio
four     nevada
five     nevada
six      nevada
Name: state, dtype: object
In [31]:
frame2.year
Out[31]:
one      2000
two      2001
three    2002
four     2001
five     2002
six      2003
Name: year, dtype: int64
In [32]:
frame2.loc['three']
Out[32]:
year     2002
state    ohio
pop       3.6
debt      NaN
Name: three, dtype: object
In [33]:
frame2['debt']=16.5
frame2
Out[33]:
year	state	pop	debt
one	2000	ohio	1.2	16.5
two	2001	ohio	1.7	16.5
three	2002	ohio	3.6	16.5
four	2001	nevada	2.4	16.5
five	2002	nevada	2.9	16.5
six	2003	nevada	3.2	16.5
In [34]:
frame2['debt']=np.arange(6.)
frame2
Out[34]:
year	state	pop	debt
one	2000	ohio	1.2	0.0
two	2001	ohio	1.7	1.0
three	2002	ohio	3.6	2.0
four	2001	nevada	2.4	3.0
five	2002	nevada	2.9	4.0
six	2003	nevada	3.2	5.0
In [35]:
val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2
Out[35]:
year	state	pop	debt
one	2000	ohio	1.2	NaN
two	2001	ohio	1.7	-1.2
three	2002	ohio	3.6	NaN
four	2001	nevada	2.4	-1.5
five	2002	nevada	2.9	-1.7
six	2003	nevada	3.2	NaN
In [36]:
frame2['eastern']=frame2.state == 'ohio'
frame2
Out[36]:
year	state	pop	debt	eastern
one	2000	ohio	1.2	NaN	True
two	2001	ohio	1.7	-1.2	True
three	2002	ohio	3.6	NaN	True
four	2001	nevada	2.4	-1.5	False
five	2002	nevada	2.9	-1.7	False
six	2003	nevada	3.2	NaN	False
In [37]:
del frame2['eastern']
frame2.columns
Out[37]:
Index(['year', 'state', 'pop', 'debt'], dtype='object')
In [38]:
pop = {'nevada':{2001:2.4,2002:2.9},
     'ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = pd.DataFrame(pop)
frame3
Out[38]:
nevada	ohio
2000	NaN	1.5
2001	2.4	1.7
2002	2.9	3.6
In [39]:
frame3.T
Out[39]:
2000	2001	2002
nevada	NaN	2.4	2.9
ohio	1.5	1.7	3.6
In [40]:
pd.DataFrame(pop,index=[2001,2002,2003])
Out[40]:
nevada	ohio
2001	2.4	1.7
2002	2.9	3.6
2003	NaN	NaN
In [41]:
pdata = {'ohio':frame3['ohio'][:-1],
        'nevada':frame3['nevada'][:2]}
pd.DataFrame(pdata)
Out[41]:
ohio	nevada
2000	1.5	NaN
2001	1.7	2.4
In [42]:
frame3.index.name = 'year';frame3.columns.name = 'state'
frame3
Out[42]:
state	nevada	ohio
year		
2000	NaN	1.5
2001	2.4	1.7
2002	2.9	3.6
In [43]:
frame3.values
Out[43]:
array([[nan, 1.5],
       [2.4, 1.7],
       [2.9, 3.6]])
In [44]:
frame2.values
Out[44]:
array([[2000, 'ohio', 1.2, nan],
       [2001, 'ohio', 1.7, -1.2],
       [2002, 'ohio', 3.6, nan],
       [2001, 'nevada', 2.4, -1.5],
       [2002, 'nevada', 2.9, -1.7],
       [2003, 'nevada', 3.2, nan]], dtype=object)
In [45]:
obj = pd.Series(range(3),index=['a','b','c'])
index = obj.index
index
Out[45]:
Index(['a', 'b', 'c'], dtype='object')
In [46]:
index[1:]
Out[46]:
Index(['b', 'c'], dtype='object')
In [47]:
labels = pd.Index(np.arange(3))
labels
Out[47]:
Int64Index([0, 1, 2], dtype='int64')
In [48]:
obj2 = pd.Series([1.5,-2.5,0],index=labels)
obj2
Out[48]:
0    1.5
1   -2.5
2    0.0
dtype: float64
