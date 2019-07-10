第10章 数据聚合与分组运算
知识补充：
分组键可以有多种形式，且类型不必相同：

列表或数组，其长度与待分组的轴一样。
表示DataFrame 某个列名的值。
字典或Series，给出待分组轴上的值与分组名之间的对应关系。
函数，用于处理轴索引或索引中的 各个标签。

代码：
In [164]:
import pandas as pd
import numpy as np
In [2]:
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                  'key2': ['one', 'two', 'one', 'two', 'one'],
                  'data1': np.random.randn(5),
                  'data2': np.random.randn(5)})

Out[2]:
    key1	key2	data1	data2
    0	a	one	0.319679	-1.054333
    1	a	two	2.048880	1.130118
      2	b	one	-1.009887	0.464170
    3	b	two	-0.064568	0.179669
    4	a	one	-1.176650	1.28716

In [3]: grouped = df['data1'].groupby(df['key1'])

Out[3]:
<pandas.core.groupby.groupby.SeriesGroupBy object at 0x0000022C77EAF4A8>
变量grouped是一个GroupBy对象。它实际上 还没有进行任何计算，只是含有一些有关分组键df['key1']的 中间数据而已。换句话说，该对象已经有了接下来对各分组执行运算 所需的 一切信息。

In [4]: grouped.mean()
Out[4]:
  key1
    a    0.397303
    b   -0.537228
    Name: data1, dtype: float64
    稍后将详细讲解 .mean()的 调用过程。这里最重要的是，数据(Series)根据分组键进行了聚合，产生了一个新的Series，其索引为key1列中的唯一值。之所以结果中索引的 名称 为key1，是因为原始DataFrame的列df['key1']就叫这个名字。

如果我们一次传入多个数组的 列表，就会得到不同的结果
In [5]:
means = df['data1'].groupby([df['key1'], df['key2']]).mean()

means
Out[5]:
        key1  key2
a     one    -0.428486
      two     2.048880
b     one    -1.009887
      two    -0.064568
Name: data1, dtype: float64
这里，通过两个键对数据进行了分组，得到的Series具有一个层次化索引(由唯一的键对组成)：
In [6]: means.unstack()
Out[6]:
      key2	one	two
      key1		
      a	-0.428486	2.048880
      b	-1.009887	-0.064568
      在这个例子中，分组键均为Series。实际上，分组键可以是任何长度适当的 数组：
      
In [7]:
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
In [8]:
df['data1'].groupby([states, years]).mean()
Out[8]:
California  2005    2.048880
            2006   -1.009887
Ohio        2005    0.127555
            2006   -1.176650
Name: data1, dtype: float64
通常，分组信息就位于相同的 要处理的DataFrame中。这里，你还可以将列名(可以是字符串、数字或其他Python对象)用作分组键：
In [10]:
df.groupby('key1').mean()
Out[10]:
data1	data2
key1		
a	0.397303	0.454317
b	-0.537228	0.321919
In [11]:
df.groupby(['key1', 'key2']).mean()
Out[11]:
data1	data2
key1	key2		
a	one	-0.428486	0.116416
two	2.048880	1.130118
b	one	-1.009887	0.464170
two	-0.064568	0.179669
你可能已经注意到了，第一个例子在执行df.groupby('key1').mean()时，结果中 没有key2列。这是因为df['key2'] 不是数值数据(俗称“麻烦列”)，所以被从结果中排除了。

默认情况下，所有数值列都会被聚合，虽然有时可能会被过滤为 一个子集，稍后就会碰到。
无论你准备拿groupby做什么，都有可能会用到GroupBy的 size方法，它可以返回一个含有分组大小的Series：
In [12]:
df.groupby(['key1', 'key2']).size()
Out[12]:
key1  key2
a     one     2
      two     1
b     one     1
      two     1
dtype: int64
