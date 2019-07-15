
In [2]:
数据聚合与分组运算

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
df
Out[2]:
key1	key2	data1	data2
0	a	one	-1.357141	0.347548
1	a	two	-0.832734	0.851675
2	b	one	1.912889	-1.222742
3	b	two	-0.337824	0.365060
4	a	one	0.836447	0.264417

In [3]:
# 假设你想要按key1进行分组，并计算data1列的平均值。实现该功能的方式有很多，而我们
# 这里要用的是：访问data1，并根据key1调用groupby
grouped = df['data1'].groupby(df['key1'])
grouped

Out[3]:
<pandas.core.groupby.generic.SeriesGroupBy object at 0x000001C83F0CC908>
In [4]:
# 变量grouped是一个GroupBy对象。它实际上还没有进行任何运算，只是含有一些有关
# 分组键df['key1']的中间数据而已，换句话说，该对象已经有了接下来对各组执行运算
# 的一切信息，我们可以调用GroupBy的mean方法计算分组平均值
grouped.mean()

Out[4]:
key1
a   -0.451143
b    0.787533
Name: data1, dtype: float64

In [5]:
# 这里最重要的是，数据（Series）根据分组键进行了聚合，产生了一个新的Series，其索引
# key1列中的唯一值。之所以结果中索引的名称为key1，是因为原始DataFrame的列就叫这个


In [6]:
# 如果我们一次传入多个数组的列表，就会得到不同的结果
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
means

Out[6]:
key1  key2
a     one    -0.260347
      two    -0.832734
b     one     1.912889
      two    -0.337824
Name: data1, dtype: float64

In [7]:
# 这里我们通过两个键对数据进行了分组，得到的Series具有一个层次化索引
means.unstack()

Out[7]:
key2	one	two
key1		
a	-0.260347	-0.832734
b	1.912889	-0.337824

In [8]:
# 在这个例子中，分组键均为Series。实际上，分组键可以是任何长度适当的数组
# states years分别对应data1中的值
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()

Out[8]:
California  2005   -0.832734
            2006    1.912889
Ohio        2005   -0.847482
            2006    0.836447
Name: data1, dtype: float64

In [9]:
# 通常，分组信息就位于相同的要处理DataFrame中。这里，你可以将列名（可以是字符串、
# 数字或其他Python对象）用作分组键
df.groupby('key1').mean()

Out[9]:
data1	data2
key1		
a	-0.451143	0.487880
b	0.787533	-0.428841
In [10]:
df.groupby(['key1', 'key2']).mean()
Out[10]:
data1	data2
key1	key2		
a	one	-0.260347	0.305982
two	-0.832734	0.851675
b	one	1.912889	-1.222742
two	-0.337824	0.365060
In [11]:
# 第一个例子在执行df.groupby('key1').mean()时，结果中没有key2列，这是因为df['key2']
# 不是数值数据（俗称“麻烦列”）所以从结果中排除了。默认情况下，所有数值列都会被
# 聚合，虽然有时可能会被过滤为一个子集，稍后就会碰到
In [12]:
# 无论你准备拿groupby做什么，都有可能会用到Groupby的size方法，它可以返回一个
# 含有分组大小的Series
df.groupby(['key1', 'key2']).size()
Out[12]:
key1  key2
a     one     2
      two     1
b     one     1
      two     1
dtype: int64
In [13]:
# 任何分组关键词中的缺失值都会被从结果中除去
In [14]:
#groupby对象支持迭代，可以产生一组二元元组（由分组名和数据块组成）
for name, group in df.groupby('key1'):
    print(name)
    print(group)
a
  key1 key2     data1     data2
0    a  one -1.357141  0.347548
1    a  two -0.832734  0.851675
4    a  one  0.836447  0.264417
b
  key1 key2     data1     data2
2    b  one  1.912889 -1.222742
3    b  two -0.337824  0.365060
In [15]:
# 对于多重键的情况，元组的第一个元素将会是由键值组成的元组
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)
('a', 'one')
  key1 key2     data1     data2
0    a  one -1.357141  0.347548
4    a  one  0.836447  0.264417
('a', 'two')
  key1 key2     data1     data2
1    a  two -0.832734  0.851675
('b', 'one')
  key1 key2     data1     data2
2    b  one  1.912889 -1.222742
('b', 'two')
  key1 key2     data1    data2
3    b  two -0.337824  0.36506
In [16]:
# 你可以对这些数据片段做任何操作。比如将这些数据片段做成一个字典
pieces = dict(list(df.groupby('key1')))
pieces
Out[16]:
{'a':   key1 key2     data1     data2
 0    a  one -1.357141  0.347548
 1    a  two -0.832734  0.851675
 4    a  one  0.836447  0.264417, 'b':   key1 key2     data1     data2
 2    b  one  1.912889 -1.222742
 3    b  two -0.337824  0.365060}
