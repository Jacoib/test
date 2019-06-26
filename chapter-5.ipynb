*-------------Chapter5-pandas----------*
In [2]: import pandas as pd
        obj = pd.Series([4,7,-5,3])
In [3]: obj
Out[3]: 0    4
        1    7
        2   -5
        3    3
       dtype: int64
In [4]: obj.values
Out[4]: array([ 4,  7, -5,  3], 
        dtype=int64)
In [5]: obj.index
Out[5]: RangeIndex(start=0, stop=4, step=1)
In [11]: obj2 = pd.Series([4,7,-5,3], 
         index=['d','b','a','c'])
In [12]: obj2
Out[12]:
d    4
b    7
a   -5
c    3
dtype: int64
In [13]: obj2.index
Out[13]:
Index(['d', 'b', 'a', 'c'], 
dtype='object')
In [14]: obj2 * 2
Out[14]:
d     8
b    14
a    -6
c    10
dtype: int64
In [15]: obj2['d'] = 2
In [17]: obj2[['c','a','d']]
Out[17]:
c    3
a   -5
d    2
dtype: int64
In [18]: obj2[obj2>0]
Out[18]:
d    2
b    7
c    3
dtype: int64
In [19]: obj2*2
Out[19]:
d     4
b    14
a   -10
c     6
dtype: int64
In [22]:import numpy as npnp.exp(obj2)
Out[22]:
d       7.389056
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
In [23]:
'b' in obj2
Out[23]:
True
In [24]:
sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
In [25]:
obj3 = pd.Series(sdata)
In [26]:
obj3
Out[26]:
Ohio      35000
Texas     71000
Oregon    16000
Utah       5000
dtype: int64
In [27]:
states = ['California','Ohio','Oregon','Texas']
In [28]:
obj4 = pd.Series(sdata, index = states)
In [29]:
obj4
Out[29]:
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
In [30]:
pd.isnull(obj4)
Out[30]:
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
In [31]:
pd.notnull(obj4)
Out[31]:
California    False
Ohio           True
Oregon         True
Texas          True
dtype: bool
In [32]:
obj4.isnull()
Out[32]:
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
In [33]:
obj3
Out[33]:
Ohio      35000
Texas     71000
Oregon    16000
Utah       5000
dtype: int64
In [34]:
obj4
Out[34]:
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
In [35]:
obj3 + obj4
Out[35]:
California         NaN
Ohio           70000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN
dtype: float64
In [36]:
obj4.name = 'population'
In [37]:
obj4.index.name = 'state'
In [38]:
obj4
Out[38]:
state
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64
In [39]:
obj
Out[39]:
0    4
1    7
2   -5
3    3
dtype: int64
In [40]:
obj.index = ['Bob','Steve','Jeff','Ryan']
In [41]:
obj
Out[41]:
Bob      4
Steve    7
Jeff    -5
Ryan     3
dtype: int64
In [42]:
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
In [43]:
frame = pd.DataFrame(data)
In [44]:
frame
Out[44]:
state	year	pop
0	Ohio	2000	1.5
1	Ohio	2001	1.7
2	Ohio	2002	3.6
3	Nevada	2001	2.4
4	Nevada	2002	2.9
5	Nevada	2003	3.2
In [45]:
frame.head
Out[45]:
<bound method NDFrame.head of     state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
5  Nevada  2003  3.2>
In [46]:
frame.head()
Out[46]:
state	year	pop
0	Ohio	2000	1.5
1	Ohio	2001	1.7
2	Ohio	2002	3.6
3	Nevada	2001	2.4
4	Nevada	2002	2.9
In [48]:
pd.DataFrame(data,columns = ['year','state','pop'])
Out[48]:
year	state	pop
0	2000	Ohio	1.5
1	2001	Ohio	1.7
2	2002	Ohio	3.6
3	2001	Nevada	2.4
4	2002	Nevada	2.9
5	2003	Nevada	3.2
In [49]:
frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
In [50]:
frame2
Out[50]:
year	state	pop	debt
one	2000	Ohio	1.5	NaN
two	2001	Ohio	1.7	NaN
three	2002	Ohio	3.6	NaN
four	2001	Nevada	2.4	NaN
five	2002	Nevada	2.9	NaN
six	2003	Nevada	3.2	NaN
In [51]:
frame2.columns
Out[51]:
Index(['year', 'state', 'pop', 'debt'], dtype='object')
In [52]:
frame2['state']
Out[52]:
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
six      Nevada
Name: state, dtype: object
In [53]:
frame2.year
Out[53]:
one      2000
two      2001
three    2002
four     2001
five     2002
six      2003
Name: year, dtype: int64
In [54]:
frame2.loc['three']
Out[54]:
year     2002
state    Ohio
pop       3.6
debt      NaN
Name: three, dtype: object
In [55]:
frame2['debt'] = 16.5
In [56]:
frame2
Out[56]:
year	state	pop	debt
one	2000	Ohio	1.5	16.5
two	2001	Ohio	1.7	16.5
three	2002	Ohio	3.6	16.5
four	2001	Nevada	2.4	16.5
five	2002	Nevada	2.9	16.5
six	2003	Nevada	3.2	16.5
In [57]:
frame2['debt'] = np.arange(6.)
In [58]:
frame2
Out[58]:
year	state	pop	debt
one	2000	Ohio	1.5	0.0
two	2001	Ohio	1.7	1.0
three	2002	Ohio	3.6	2.0
four	2001	Nevada	2.4	3.0
five	2002	Nevada	2.9	4.0
six	2003	Nevada	3.2	5.0
In [59]:
val = pd.Series([-1.2, -1.5, -1.7], index=['two','four','five'])
In [61]:
frame2['debt'] = val
In [62]:
frame2
Out[62]:
year	state	pop	debt
one	2000	Ohio	1.5	NaN
two	2001	Ohio	1.7	-1.2
three	2002	Ohio	3.6	NaN
four	2001	Nevada	2.4	-1.5
five	2002	Nevada	2.9	-1.7
six	2003	Nevada	3.2	NaN
In [64]:
frame2['eastern'] = frame2.state =='Ohio'
In [65]:
frame2
Out[65]:
year	state	pop	debt	eastern
one	2000	Ohio	1.5	NaN	True
two	2001	Ohio	1.7	-1.2	True
three	2002	Ohio	3.6	NaN	True
four	2001	Nevada	2.4	-1.5	False
five	2002	Nevada	2.9	-1.7	False
six	2003	Nevada	3.2	NaN	False
In [66]:
del frame2['eastern']
In [67]:
frame2.columns
Out[67]:
Index(['year', 'state', 'pop', 'debt'], dtype='object')
In [68]:
pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
In [69]:
frame3 = pd.DataFrame(pop)
In [70]:
frame3
Out[70]:
Nevada	Ohio
2000	NaN	1.5
2001	2.4	1.7
2002	2.9	3.6
In [71]:
frame3.T
Out[71]:
2000	2001	2002
Nevada	NaN	2.4	2.9
Ohio	1.5	1.7	3.6
In [72]:
pd.DataFrame(pop,index=[2001,2002,2003])
Out[72]:
Nevada	Ohio
2001	2.4	1.7
2002	2.9	3.6
2003	NaN	NaN
In [73]:
pdata = {'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
In [74]:
pdata
Out[74]:
{'Ohio': 2000    1.5
 2001    1.7
 Name: Ohio, dtype: float64, 'Nevada': 2000    NaN
 2001    2.4
 Name: Nevada, dtype: float64}
In [75]:
pd.DataFrame(pdata)
Out[75]:
Ohio	Nevada
2000	1.5	NaN
2001	1.7	2.4
In [76]:
frame3.index.name = 'year';frame3.columns.name ='state'
In [77]:
frame3
Out[77]:
state	Nevada	Ohio
year		
2000	NaN	1.5
2001	2.4	1.7
2002	2.9	3.6
In [78]:
frame3.values
Out[78]:
array([[nan, 1.5],
       [2.4, 1.7],
       [2.9, 3.6]])
In [79]:
frame2.values
Out[79]:
array([[2000, 'Ohio', 1.5, nan],
       [2001, 'Ohio', 1.7, -1.2],
       [2002, 'Ohio', 3.6, nan],
       [2001, 'Nevada', 2.4, -1.5],
       [2002, 'Nevada', 2.9, -1.7],
       [2003, 'Nevada', 3.2, nan]], dtype=object)
In [80]:
obj = pd.Series(range(3), index=['a','b','c'])
In [82]:
index =obj.index
In [83]:
index
Out[83]:
Index(['a', 'b', 'c'], dtype='object')
In [84]:
index[1:]
Out[84]:
Index(['b', 'c'], dtype='object')
In [85]:
labels = pd.Index(np.arange(3))
In [86]:
labels
Out[86]:
Int64Index([0, 1, 2], dtype='int64')
In [87]:
obj2 = pd.Series([1.5,-2.5,0],index = labels)
In [88]:
obj2
Out[88]:
0    1.5
1   -2.5
2    0.0
dtype: float64
In [89]:
obj2.index is labels
Out[89]:
True
In [90]:
frame3
Out[90]:
state	Nevada	Ohio
year		
2000	NaN	1.5
2001	2.4	1.7
2002	2.9	3.6
In [91]:
frame3.columns
Out[91]:
Index(['Nevada', 'Ohio'], dtype='object', name='state')
In [93]:
'Ohio' in frame3.columns
Out[93]:
True
In [94]:
2003 in frame3.index
Out[94]:
False
In [95]:
dup_labels = pd.Index(['foo','foo','bar','bar'])
In [96]:
dup_labels
Out[96]:
Index(['foo', 'foo', 'bar', 'bar'], dtype='object')
In [98]:
obj = pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
In [99]:
obj
Out[99]:
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
In [100]:
obj2 = obj.reindex(['a','b','c','d','e'])
In [101]:
obj2
Out[101]:
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
In [102]:
obj3 = pd.Series(['blue','purple','yellow'],index = [0,2,4])
In [103]:
obj3
Out[103]:
0      blue
2    purple
4    yellow
dtype: object
In [104]:
obj3.reindex(range(6),method = 'ffill')
Out[104]:
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
In [105]:
obj3
Out[105]:
0      blue
2    purple
4    yellow
dtype: object
In [106]:
frame = pd.DataFrame(np.arange(9).reshape((3,3)),index = ['a','b','c'],columns = ['Ohio','Texas','California'])
In [107]:
frame
Out[107]:
Ohio	Texas	California
a	0	1	2
b	3	4	5
c	6	7	8
In [108]:
frame2 = frame.reindex(['a','b','c','d'])
In [109]:
frame2
Out[109]:
Ohio	Texas	California
a	0.0	1.0	2.0
b	3.0	4.0	5.0
c	6.0	7.0	8.0
d	NaN	NaN	NaN
In [110]:
states = ['Texas','Utah','California']
In [111]:
frame.reindex(columns=states)
Out[111]:
Texas	Utah	California
a	1	NaN	2
b	4	NaN	5
c	7	NaN	8
In [112]:
frame.loc[['a','b','c','d'],states]
c:\users\闫少伟\appdata\local\programs\python\python37\lib\site-packages\pandas\core\indexing.py:1494: FutureWarning: 
Passing list-likes to .loc or [] with any missing label will raise
KeyError in the future, you can use .reindex() as an alternative.

See the documentation here:
https://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate-loc-reindex-listlike
  return self._getitem_tuple(key)
Out[112]:
Texas	Utah	California
a	1.0	NaN	2.0
b	4.0	NaN	5.0
c	7.0	NaN	8.0
d	NaN	NaN	NaN
In [113]:
obj = pd.Series(np.arange(5.),index=['a','b','c','d','e'])
In [114]:
obj
Out[114]:
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64
In [116]:
new_obj = obj.drop('c')
In [117]:
new_obj
Out[117]:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
In [118]:
obj.drop(['d','c'])
Out[118]:
a    0.0
b    1.0
e    4.0
dtype: float64
In [119]:
data = pd.DataFrame(np.arange(16).reshape(4,4),index = ['Ohio','colorado','Utah','New York'],columns = ['one','two','three','four'])
In [120]:
data
Out[120]:
one	two	three	four
Ohio	0	1	2	3
colorado	4	5	6	7
Utah	8	9	10	11
New York	12	13	14	15
In [122]:
data.drop(['colorado','Ohio'])
Out[122]:
one	two	three	four
Utah	8	9	10	11
New York	12	13	14	15
In [125]:
data.drop('two',axis=1)
Out[125]:
one	three	four
Ohio	0	2	3
colorado	4	6	7
Utah	8	10	11
New York	12	14	15
In [126]:
data.drop(['two','four'],axis = 'columns')
Out[126]:
one	three
Ohio	0	2
colorado	4	6
Utah	8	10
New York	12	14
In [127]:
obj.drop('c',inplace =True)
In [128]:
obj
Out[128]:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
In [129]:
obj = pd.Series(np.arange(5.),index= ['a','b','c','d','e'])
In [130]:
obj
Out[130]:
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64
In [131]:
new_obj=obj.drop('c')
In [132]:
new_obj
Out[132]:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
In [135]:
obj.drop(['d','c'])
Out[135]:
a    0.0
b    1.0
e    4.0
dtype: float64
In [136]:
obj['b']
Out[136]:
1.0
In [137]:
obj[1]
Out[137]:
1.0
In [138]:
obj[2:4]
Out[138]:
c    2.0
d    3.0
dtype: float64
In [139]:
obj[['b','a','d']]
Out[139]:
b    1.0
a    0.0
d    3.0
dtype: float64
In [140]:
obj[[1,3]]
Out[140]:
b    1.0
d    3.0
dtype: float64
In [141]:
obj[obj<2]
Out[141]:
a    0.0
b    1.0
dtype: float64
In [142]:
obj['b':'c']
Out[142]:
b    1.0
c    2.0
dtype: float64
In [143]:
obj['b':'c']=5
In [144]:
obj
Out[144]:
a    0.0
b    5.0
c    5.0
d    3.0
e    4.0
dtype: float64
In [145]:
data = pd.DataFrame(np.arange(16).reshape(4,4),index = ['Ohio','colorado','Utah','New York'],columns = ['one','two','three','four'])
In [146]:
data
Out[146]:
one	two	three	four
Ohio	0	1	2	3
colorado	4	5	6	7
Utah	8	9	10	11
New York	12	13	14	15
In [147]:
data['two']
Out[147]:
Ohio         1
colorado     5
Utah         9
New York    13
Name: two, dtype: int32
In [148]:
data[['three','one']]
Out[148]:
three	one
Ohio	2	0
colorado	6	4
Utah	10	8
New York	14	12
In [149]:
data[:2]
Out[149]:
one	two	three	four
Ohio	0	1	2	3
colorado	4	5	6	7
In [150]:
data[data['three']>5]
Out[150]:
one	two	three	four
colorado	4	5	6	7
Utah	8	9	10	11
New York	12	13	14	15
In [151]:
data<5
Out[151]:
one	two	three	four
Ohio	True	True	True	True
colorado	True	False	False	False
Utah	False	False	False	False
New York	False	False	False	False
In [152]:
data[data<5] = 0
In [153]:
data
Out[153]:
one	two	three	four
Ohio	0	0	0	0
colorado	0	5	6	7
Utah	8	9	10	11
New York	12	13	14	15
In [155]:
data.loc['colorado',['two','three']]
Out[155]:
two      5
three    6
Name: colorado, dtype: int32
In [156]:
data.iloc[2,[3,0,1]]
Out[156]:
four    11
one      8
two      9
Name: Utah, dtype: int32
In [157]:
data.iloc[2]
Out[157]:
one       8
two       9
three    10
four     11
Name: Utah, dtype: int32
In [158]:
data.iloc[[1,2],[3,0,1]]
Out[158]:
four	one	two
colorado	7	0	5
Utah	11	8	9
In [159]:
data.loc[:'Utah','two']
Out[159]:
Ohio        0
colorado    5
Utah        9
Name: two, dtype: int32
In [160]:
data.iloc[:,:3][data.three>5]
Out[160]:
one	two	three
colorado	0	5	6
Utah	8	9	10
New York	12	13	14
In [161]:
ser = pd.Series(np.arange(3.))
In [162]:
ser
Out[162]:
0    0.0
1    1.0
2    2.0
dtype: float64
In [164]:
ser2 = pd.Series(np.arange(3.),index = ['a','b','c'])
In [165]:
ser2
Out[165]:
a    0.0
b    1.0
c    2.0
dtype: float64
In [166]:
ser2[-1]
Out[166]:
2.0
In [167]:
ser[:1]
Out[167]:
0    0.0
dtype: float64
In [168]:
ser.loc[:1]
Out[168]:
0    0.0
1    1.0
dtype: float64
In [169]:
ser.iloc[:1]
Out[169]:
0    0.0
dtype: float64
In [170]:
s1 = pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
In [171]:
s2 = pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
In [172]:
s1
Out[172]:
a    7.3
c   -2.5
d    3.4
e    1.5
dtype: float64
In [173]:
s2
Out[173]:
a   -2.1
c    3.6
e   -1.5
f    4.0
g    3.1
dtype: float64
In [174]:
s1+s2
Out[174]:
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
In [175]:
df1 = pd.DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])
In [176]:
df2 = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
In [177]:
df1
Out[177]:
b	c	d
Ohio	0.0	1.0	2.0
Texas	3.0	4.0	5.0
Colorado	6.0	7.0	8.0
In [178]:
df2
Out[178]:
b	d	e
Utah	0.0	1.0	2.0
Ohio	3.0	4.0	5.0
Texas	6.0	7.0	8.0
Oregon	9.0	10.0	11.0
In [179]:
df1+df2
Out[179]:
b	c	d	e
Colorado	NaN	NaN	NaN	NaN
Ohio	3.0	NaN	6.0	NaN
Oregon	NaN	NaN	NaN	NaN
Texas	9.0	NaN	12.0	NaN
Utah	NaN	NaN	NaN	NaN
In [180]:
df1 = pd.DataFrame({'A':[1,2]})
In [181]:
df2 = pd.DataFrame({'B':[3,4]})
In [182]:
df1
Out[182]:
A
0	1
1	2
In [183]:
df2
Out[183]:
B
0	3
1	4
In [184]:
df1-df2
Out[184]:
A	B
0	NaN	NaN
1	NaN	NaN
In [185]:
df1 = pd.DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
In [186]:
df2 = pd.DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
In [187]:
df2.loc[1,'b'] = np.nan
In [188]:
df1
Out[188]:
a	b	c	d
0	0.0	1.0	2.0	3.0
1	4.0	5.0	6.0	7.0
2	8.0	9.0	10.0	11.0
In [189]:
df2
Out[189]:
a	b	c	d	e
0	0.0	1.0	2.0	3.0	4.0
1	5.0	NaN	7.0	8.0	9.0
2	10.0	11.0	12.0	13.0	14.0
3	15.0	16.0	17.0	18.0	19.0
In [190]:
df1.add(df2,fill_value=0)
Out[190]:
a	b	c	d	e
0	0.0	2.0	4.0	6.0	4.0
1	9.0	5.0	13.0	15.0	9.0
2	18.0	20.0	22.0	24.0	14.0
3	15.0	16.0	17.0	18.0	19.0
In [191]:
1/df1
Out[191]:
a	b	c	d
0	inf	1.000000	0.500000	0.333333
1	0.250	0.200000	0.166667	0.142857
2	0.125	0.111111	0.100000	0.090909
In [192]:
df1.rdiv(1)
Out[192]:
a	b	c	d
0	inf	1.000000	0.500000	0.333333
1	0.250	0.200000	0.166667	0.142857
2	0.125	0.111111	0.100000	0.090909
In [193]:
df1.reindex(columns=df2.columns,fill_value=0)
Out[193]:
a	b	c	d	e
0	0.0	1.0	2.0	3.0	0
1	4.0	5.0	6.0	7.0	0
2	8.0	9.0	10.0	11.0	0
In [194]:
arr = np.arange(12.).reshape((3,4))
In [195]:
arr
Out[195]:
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])
In [196]:
arr[0]
Out[196]:
array([0., 1., 2., 3.])
In [197]:
arr-arr[0]
Out[197]:
array([[0., 0., 0., 0.],
       [4., 4., 4., 4.],
       [8., 8., 8., 8.]])
In [198]:
frame = pd.DataFrame(np.arange(12.).reshape(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
In [199]:
series = frame.iloc[0]
In [200]:
series
Out[200]:
b    0.0
d    1.0
e    2.0
Name: Utah, dtype: float64
In [201]:
frame
Out[201]:
b	d	e
Utah	0.0	1.0	2.0
Ohio	3.0	4.0	5.0
Texas	6.0	7.0	8.0
Oregon	9.0	10.0	11.0
In [202]:
frame-series
Out[202]:
b	d	e
Utah	0.0	0.0	0.0
Ohio	3.0	3.0	3.0
Texas	6.0	6.0	6.0
Oregon	9.0	9.0	9.0
In [203]:
series2 = pd.Series(range(3),index=['b','e','f'])
In [204]:
frame+series2
Out[204]:
b	d	e	f
Utah	0.0	NaN	3.0	NaN
Ohio	3.0	NaN	6.0	NaN
Texas	6.0	NaN	9.0	NaN
Oregon	9.0	NaN	12.0	NaN
In [205]:
series3 = frame['d']
In [206]:
series3
Out[206]:
Utah       1.0
Ohio       4.0
Texas      7.0
Oregon    10.0
Name: d, dtype: float64
In [207]:
frame.sub(series3,axis='index')
Out[207]:
b	d	e
Utah	-1.0	0.0	1.0
Ohio	-1.0	0.0	1.0
Texas	-1.0	0.0	1.0
Oregon	-1.0	0.0	1.0
In [210]:
frame = pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
In [211]:
frame
Out[211]:
b	d	e
Utah	0.225388	-0.367365	0.523710
Ohio	-0.261241	0.807976	0.749540
Texas	-0.301367	0.630703	0.180248
Oregon	-0.752462	-0.065230	0.120138
In [212]:
np.abs(frame)
Out[212]:
b	d	e
Utah	0.225388	0.367365	0.523710
Ohio	0.261241	0.807976	0.749540
Texas	0.301367	0.630703	0.180248
Oregon	0.752462	0.065230	0.120138
In [213]:
f=lambda x:x.max()-x.min()
In [216]:
frame.apply(f)
Out[216]:
b    0.977850
d    1.175342
e    0.629402
dtype: float64
In [217]:
frame.apply(f,axis='columns')
Out[217]:
Utah      0.891076
Ohio      1.069217
Texas     0.932070
Oregon    0.872601
dtype: float64
In [218]:
format = lambda x:'%.2f'%x
In [219]:
frame.applymap(format)
Out[219]:
b	d	e
Utah	0.23	-0.37	0.52
Ohio	-0.26	0.81	0.75
Texas	-0.30	0.63	0.18
Oregon	-0.75	-0.07	0.12
In [220]:
frame['e'].map(format)
Out[220]:
Utah      0.52
Ohio      0.75
Texas     0.18
Oregon    0.12
Name: e, dtype: object
In [221]:
obj = pd.Series(range(4),index=['d','a','b','c'])
In [223]:
obj.sort_index()
Out[223]:
a    1
b    2
c    3
d    0
dtype: int64
In [224]:
frame = pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
In [225]:
frame.sort_index()
Out[225]:
d	a	b	c
one	4	5	6	7
three	0	1	2	3
In [226]:
frame.sort_index(axis=1)
Out[226]:
a	b	c	d
three	1	2	3	0
one	5	6	7	4
In [227]:
frame.sort_index(axis=1,ascending=False)
Out[227]:
d	c	b	a
three	0	3	2	1
one	4	7	6	5
In [228]:
obj.sort_values()
Out[228]:
d    0
a    1
b    2
c    3
dtype: int64
In [234]:
obj = pd.Series([4, np.nan,7, np.nan,-3,2])
In [236]:
obj.sort_values()
Out[236]:
4   -3.0
5    2.0
0    4.0
2    7.0
1    NaN
3    NaN
dtype: float64
In [237]:
frame = pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
In [238]:
frame
Out[238]:
b	a
0	4	0
1	7	1
2	-3	0
3	2	1
In [239]:
frame.sort_values(by='b')
Out[239]:
b	a
2	-3	0
3	2	1
0	4	0
1	7	1
In [240]:
frame.sort_values(by=['a','b'])
Out[240]:
b	a
2	-3	0
0	4	0
3	2	1
1	7	1
In [241]:
obj = pd.Series([7,-5,7,4,2,0,4])
In [242]:
obj.rank()
Out[242]:
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64
In [243]:
obj.rank(method='first')
Out[243]:
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64
In [244]:
obj.rank(ascending=False,method='max')
Out[244]:
0    2.0
1    7.0
2    2.0
3    4.0
4    5.0
5    6.0
6    4.0
dtype: float64
In [245]:
frame = pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})
In [246]:
frame
Out[246]:
b	a	c
0	4.3	0	-2.0
1	7.0	1	5.0
2	-3.0	0	8.0
3	2.0	1	-2.5
In [247]:
frame.rank(axis='columns')
Out[247]:
b	a	c
0	3.0	2.0	1.0
1	3.0	1.0	2.0
2	1.0	2.0	3.0
3	3.0	2.0	1.0
In [248]:
obj = pd.Series(range(5),index=['a','a','b','b','c'])
In [249]:
obj
Out[249]:
a    0
a    1
b    2
b    3
c    4
dtype: int64
In [250]:
obj.index.is_unique
Out[250]:
False
In [251]:
obj['a']
Out[251]:
a    0
a    1
dtype: int64
In [252]:
obj['c']
Out[252]:
4
In [253]:
df = pd.DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
In [254]:
df
Out[254]:
0	1	2
a	2.045207	1.061667	-1.155161
a	0.553602	-0.770188	-0.913436
b	0.398062	-0.016016	-0.752281
b	-0.111562	1.537161	1.321559
In [255]:
df.loc['b']
Out[255]:
0	1	2
b	0.398062	-0.016016	-0.752281
b	-0.111562	1.537161	1.321559
In [256]:
df = pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
In [257]:
df
Out[257]:
one	two
a	1.40	NaN
b	7.10	-4.5
c	NaN	NaN
d	0.75	-1.3
In [258]:
df.sum()
Out[258]:
one    9.25
two   -5.80
dtype: float64
In [259]:
df.sum(axis='columns')
Out[259]:
a    1.40
b    2.60
c    0.00
d   -0.55
dtype: float64
In [260]:
df.mean(axis='columns',skipna=False)
Out[260]:
a      NaN
b    1.300
c      NaN
d   -0.275
dtype: float64
In [261]:
df.idxmax()
Out[261]:
one    b
two    d
dtype: object
In [262]:
df.cumsum()
Out[262]:
one	two
a	1.40	NaN
b	8.50	-4.5
c	NaN	NaN
d	9.25	-5.8
In [263]:
df.describe()
Out[263]:
one	two
count	3.000000	2.000000
mean	3.083333	-2.900000
std	3.493685	2.262742
min	0.750000	-4.500000
25%	1.075000	-3.700000
50%	1.400000	-2.900000
75%	4.250000	-2.100000
max	7.100000	-1.300000
In [264]:
obj = pd.Series(['a','a','b','c']*4)
In [265]:
obj
Out[265]:
0     a
1     a
2     b
3     c
4     a
5     a
6     b
7     c
8     a
9     a
10    b
11    c
12    a
13    a
14    b
15    c
dtype: object
In [266]:
obj.describe()
Out[266]:
count     16
unique     3
top        a
freq       8
dtype: object
In [267]:
import pandas_datareader.data as web
In [268]:
all_data = {ticker:web.get_data_yahoo(ticker) for ticker in ['AAPL','IBM','MSFT','GOOG']}
In [269]:
price = pd.DataFrame({ticker:data['Adj Close'] for ticker,data in all_data.items()})
In [272]:
returns = price.pct_change()
In [273]:
returns.tail()
Out[273]:
AAPL	IBM	MSFT	GOOG
Date				
2019-06-20	0.008036	0.012912	0.009286	0.008246
2019-06-21	-0.003409	0.002521	0.000146	0.009411
2019-06-24	-0.001006	0.001078	0.005914	-0.005669
2019-06-25	-0.015158	-0.007104	-0.031572	-0.026149
2019-06-26	0.023010	0.003036	0.011092	-0.005762
In [274]:
returns['MSFT'].corr(returns['IBM'])
Out[274]:
0.48706920758266603
In [275]:
returns['MSFT'].cov(returns['IBM'])
Out[275]:
8.678315536490012e-05
In [276]:
returns.MSFT.corr(returns.IBM)
Out[276]:
0.48706920758266603
In [277]:
returns.corr()
Out[277]:
AAPL	IBM	MSFT	GOOG
AAPL	1.000000	0.375461	0.453324	0.457518
IBM	0.375461	1.000000	0.487069	0.403054
MSFT	0.453324	0.487069	1.000000	0.537829
GOOG	0.457518	0.403054	0.537829	1.000000
In [278]:
returns.cov()
Out[278]:
AAPL	IBM	MSFT	GOOG
AAPL	0.000270	0.000076	0.000108	0.000116
IBM	0.000076	0.000152	0.000087	0.000077
MSFT	0.000108	0.000087	0.000209	0.000120
GOOG	0.000116	0.000077	0.000120	0.000239
In [279]:
returns.corrwith(returns.IBM)
Out[279]:
AAPL    0.375461
IBM     1.000000
MSFT    0.487069
GOOG    0.403054
dtype: float64
In [282]:
volume = pd.DataFrame({ticker:data['Volume']for ticker,data in all_data.items()})
returns.corrwith(volume)
Out[282]:
AAPL   -0.060035
IBM    -0.156182
MSFT   -0.090397
GOOG   -0.020318
dtype: float64
In [283]:
obj = pd.Series(['c','a','d','a','a','b','b','c','c'])
In [284]:
uniques = obj.unique()
In [285]:
uniques
Out[285]:
array(['c', 'a', 'd', 'b'], dtype=object)
In [286]:
obj.value_counts()
Out[286]:
a    3
c    3
b    2
d    1
dtype: int64
In [287]:
pd.value_counts(obj.values,sort =False)
Out[287]:
c    3
a    3
d    1
b    2
dtype: int64
In [288]:
obj
Out[288]:
0    c
1    a
2    d
3    a
4    a
5    b
6    b
7    c
8    c
dtype: object
In [290]:
mask = obj.isin(['b','c'])
In [291]:
mask
Out[291]:
0     True
1    False
2    False
3    False
4    False
5     True
6     True
7     True
8     True
dtype: bool
In [292]:
obj[mask]
Out[292]:
0    c
5    b
6    b
7    c
8    c
dtype: object
In [293]:
to_match =pd.Series(['c','a','b','b','c','a'])
In [294]:
unique_vals = pd.Series(['c','b','a'])
In [295]:
pd.Index(unique_vals).get_indexer(to_match)
Out[295]:
array([0, 2, 1, 1, 0, 2], dtype=int64)
In [296]:
data = pd.DataFrame({'Qu1':[1,3,4,3,4],'Qu2':[2,3,1,2,3],'Qu3':[1,5,2,4,4]})
In [297]:
data
Out[297]:
Qu1	Qu2	Qu3
0	1	2	1
1	3	3	5
2	4	1	2
3	3	2	4
4	4	3	4
In [298]:
result=data.apply(pd.value_counts).fillna(0)
In [299]:
result
Out[299]:
Qu1	Qu2	Qu3
1	1.0	1.0	1.0
2	0.0	2.0	1.0
3	2.0	2.0	0.0
4	2.0	0.0	2.0
5	0.0	0.0	1.0
In [ ]:
