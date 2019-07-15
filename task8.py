In [1]:  绘图和可视化  matplotlib 和基于它的库

In [1]:  import matplotlib.pyplot as plt
import numpy as np

In [13]:  data = np.arange(10)data

Out[13]:
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [18]:
plt.plot(data)
<IPython.core.display.Javascript object>

Out[18]:
[<matplotlib.lines.Line2D at 0x1bd725aef98>]
In [ ]:
# matplotlib的图像都位于Figure对象中，你可以用plt.figure创建一个新的Figure

In [25]:
fig = plt.figure()
<IPython.core.display.Javascript object>

In [22]:
# plt.figure有一些选项，特别是figsize，它用于确保当图片保存到磁盘时具有一定的大小
# 和纵横比，不能通过空Figure绘图，必须用add_subplot创建一个或多个subplot
ax1 = fig.add_subplot(2, 2, 1)


In [38]:
# 如果这时执行一条绘图命令（如plt.plot([1.5, 3.5, -2, 1.6])）, matplotlib就会在
# 最后一个用过的subplot（如果没有则创建一个）上进行绘制，隐藏创建figure和subplot
# 过程。因此，如果我们执行下列命令
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
<IPython.core.display.Javascript object>

Out[38]:
[<matplotlib.lines.Line2D at 0x1bd72aab828>]
In [40]:
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
<IPython.core.display.Javascript object>
