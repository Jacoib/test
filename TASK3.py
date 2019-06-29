*文件加载、存储与文件格式*

In [10]:import numpy as np
				import pandas as pd 
				from pandas import Series,DataFrame
				
In [16]:type examples\ex1
a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo

In [18]:df = pd.read_csv('examples\ex1)
				df   #以逗号分隔，使用read_csv将其读入一个DataFrame
Out[18]:
a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo
In [129]:pd.read_table('ex\ex1',sep=',')  
Out[129]:
a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

In [21]:!type examples\ex2
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
In [23]:	pd.read_csv('examples\ex2',header=None)   #读入该文件可以让pandas为其分配默认的列名
Out[23]:
0	1	2	3	4
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo
In [25]:	pd.read_csv('examples\ex2',names=['a','b','c','d','messags']) #也可以用names=[] 为其定义列名
Out[25]:
a	b	c	d	messags
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo

In [27]:
names = ['a','b','c','d','message']
pd.read_csv('examples\ex2',names=names,index_col='message') #index_col  索引列
Out[27]:
a	b	c	d
message				
hello	1	2	3	4
world	5	6	7	8
foo	9	10	11	12
将多个列做成一个层次化索引，只需传入由列编号或列名组成的列表即可：

In [28]:
!type examples\csv_mindex
key1,key2,value1,value2
out[28]:
one,a,1,2
one,b,3,4
one,c,5,6
one,d,7,8
two,a,9,10
two,b,11,12
two,c,13,14
two,d,15,16
In [29]:
parsed=pd.read_csv('examples\csv_mindex',index_col = ['key1','key2'])
parsed
Out[29]:
value1	value2
key1	key2		
one	a	1	2
b	3	4
c	5	6
d	7	8
two	a	9	10
b	11	12
c	13	14
d	15	16
In [30]:
list(open('examples\ex3.txt'))
Out[30]:
['            A         B         C\n',
 'aaa -0.264438 -1.026059 -0.619500\n',
 'bbb  0.927272  0.302904 -0.032399\n',
 'ccc -0.264273 -0.386314 -0.217601\n',
 'ddd -0.871858 -0.348382  1.100491\n']
In [31]:
result = pd.read_table('examples\ex3.txt',sep='\s+')
result

Out[31]:
A	B	C
aaa	-0.264438	-1.026059	-0.619500
bbb	0.927272	0.302904	-0.032399
ccc	-0.264273	-0.386314	-0.217601
ddd	-0.871858	-0.348382	1.100491
In [32]:
!type examples\ex4
# hey!
a,b,c,d,message
# just wanted to make things more difficult for you
# who reads CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
In [33]:
pd.read_csv('examples\ex4',skiprows=[0,2,3]) #用skiprows=[] 来跳过文件的哪些行
Out[33]:
a	b	c	d	message
0	1	2	3	4	hello
1	5	6	7	8	world
2	9	10	11	12	foo
缺失值的处理

In [34]:
!type examples\ex5.csv
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo
In [36]:
result = pd.read_csv('examples\ex5.csv')
result        
Out[36]:
something	a	b	c	d	message
0	one	1	2	3.0	4	NaN
1	two	5	6	NaN	8	world
2	three	9	10	11.0	12	foo
In [37]:
pd.isnull(result)
Out[37]:
something	a	b	c	d	message
0	False	False	False	False	False	True
1	False	False	False	True	False	False
2	False	False	False	False	False	False
na_values可以用一个列表或集合的字符串表示缺失值： 将数组中的数据改成NaN！！

In [49]:
result = pd.read_csv('examples\ex5.csv',na_values=['null'])
result
Out[49]:
something	a	b	c	d	message
0	one	1	2	3.0	4	NaN
1	two	5	6	NaN	8	world
2	three	9	10	11.0	12	foo
In [48]:
result = pd.read_csv('examples\ex5.csv',na_values='foo')
result   #将foo替换成缺失值
Out[48]:
something	a	b	c	d	message
0	one	1	2	3.0	4	NaN
1	two	5	6	NaN	8	world
2	three	9	10	11.0	12	NaN
In [50]:
sentinels = {'message':['foo','NA'],'something':['two']}
pd.read_csv('examples\ex5.csv',na_values = sentinels)      
Out[50]:
something	a	b	c	d	message
0	one	1	2	3.0	4	NaN
1	NaN	5	6	NaN	8	world
2	three	9	10	11.0	12	NaN
逐块读取文本文件
In [51]:
pd.options.display.max_rows = 10
In [52]:
result = pd.read_csv('examples\ex6.csv')
result
Out[52]:
one	two	three	four	key
0	0.467976	-0.038649	-0.295344	-1.824726	L
1	-0.358893	1.404453	0.704965	-0.200638	B
2	-0.501840	0.659254	-0.421691	-0.057688	G
3	0.204886	1.074134	1.388361	-0.982404	R
4	0.354628	-0.133116	0.283763	-0.837063	Q
...	...	...	...	...	...
9995	2.311896	-0.417070	-1.409599	-0.515821	L
9996	-0.479893	-0.650419	0.745152	-0.646038	E
9997	0.523331	0.787112	0.486066	1.093156	K
9998	-0.362559	0.598894	-1.843201	0.887292	G
9999	-0.096376	-1.012999	-0.657431	-0.573315	0
10000 rows × 5 columns

In [53]:
pd.read_csv('examples\ex6.csv',nrows=5)  
Out[53]:
one	two	three	four	key
0	0.467976	-0.038649	-0.295344	-1.824726	L
1	-0.358893	1.404453	0.704965	-0.200638	B
2	-0.501840	0.659254	-0.421691	-0.057688	G
3	0.204886	1.074134	1.388361	-0.982404	R
4	0.354628	-0.133116	0.283763	-0.837063	Q
要逐块读取文件，可以指定chunksize（行数）

In [56]:
chunker = pd.read_csv('examples\ex6.csv',chunksize=1000)
chunker
Out[56]:
<pandas.io.parsers.TextFileReader at 0x8f9bfd0>
In [59]:
chunker = pd.read_csv('examples\ex6.csv',chunksize=1000)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value=0)
tot = tot.sort_values(ascending = False)    
tot[:10]
Out[59]:
E    368.0
X    364.0
L    346.0
O    343.0
Q    340.0
M    338.0
J    337.0
F    335.0
K    334.0
H    330.0
dtype: float64
将数据写出到文本格式
In [61]:
data = pd.read_csv('examples\ex5.csv')
data
Out[61]:
something	a	b	c	d	message
0	one	1	2	3.0	4	NaN
1	two	5	6	NaN	8	world
2	three	9	10	11.0	12	foo
In [63]:
data.to_csv('examples\out.csv')
!type examples\out.csv       
,something,a,b,c,d,message
0,one,1,2,3.0,4,
1,two,5,6,,8,world
2,three,9,10,11.0,12,foo
In [65]:
import sys 
data.to_csv(sys.stdout,sep='|')  #用其他分隔符 sep=
|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6||8|world
2|three|9|10|11.0|12|foo
In [66]:
data.to_csv(sys.stdout,na_rep = 'NULL')   
,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo
In [67]:
data.to_csv(sys.stdout,index=False,header=False) 
one,1,2,3.0,4,
two,5,6,,8,world
