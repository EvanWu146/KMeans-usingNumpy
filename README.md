# README

## 任务描述

### 题目 4 ：聚类

我们已经学习过无监督学习、K-means 和 GMM。本题目要求对 cluster.dat 进行 聚类。cluster.dat 包含了若干二维输入数据（但不包含其输出）。

#### 方法 1

K-means (20 points) 使用 K-means 模型进行聚类。尝试使用不同的类别个数 K，并分析聚类结果。

#### 附加题 (BONUS: 10 points) 

按照 8:2 的比例，随机将数据划分为训练集和测试集。至少尝试 3 个不同的 K 值， 并画出不同 K 下的聚类结果，及不同模型在训练集和测试集上的损失。对结果进 行讨论，发现能解释数据的最好的 K 值。



## 实验环境

Macintosh 12.4

ARM-python 3.8

调用库：

```python
import numpy as np
import matplotlib.pyplot as plt
from math import floor
```



## 方法描述

1. 从给定的cluster.dat文件读取数据集，使用readlines方式读取，并将字符串形式的数据转化为str格式；
2. 获取两个点集之间的欧式距离：

```python
def getDistance(A, B)
```

输入：点集A，点集B

要求：点集A和点集B的shape必须相同。

返回：点集的距离列表（如果只有一个距离值则是float形式）

3. 随机获取中心点：

```python
def randomCenter(data, k)
```

调用randomInteger获取k个随机index值，随后在数据集data中取出对应的数据值。

输入：数据集data，中心点个数k

返回：选中的中心点列表

4. 获取随机整数：

```python
def randomInteger(low, high, length)
```

使用np.random.randint获取给定范围内的给定个数整数。

问题：取值个数越大，np.random.randint越可能会取到相同的随机数值。

解决：不断取值、加入随机数列表中，当现在的随机数列表长度等于length时停止返回。

输入：随机数下限low（包括），随机数上限high（不包括），随机数取值列表长度length

返回：随机数取值列表

5. 获取数据集的新中心：

```python
def newCenter(typeList, data, K)
```

用于KMeans算法中重新获取类聚中心，使用平均值方式计算。

输入：类聚类型列表typeList（记录了已分类好数据的类别号，大于0的整数），数据集data，类聚数K

输出：新的中心列表

6. KMeans主算法：

```python
def KMeans(data, K)
```

重复一下过程：

​	类聚、计算每个类的中心点，然后使用平均方法计算新的中心点；

​	新旧中心点的欧式距离在1以内，合格的中心点数+1；

直到合格的中心点数等于K，算法结束。

输入：数据集data，类聚数K

输出：类别标号typeList，中心点K

7. 在坐标系中展示类聚结果

```python
def drawPoint(data, label, center)
```

输入：数据集data，分类类别标号label，中心点center

输出：plt图展示，用不同的颜色显示数据集中不同类别的点以及中心点。

8. 分割训练集测试集，进行训练和测试，并展示结果：

```python
def fit_predict(data, K, ratio=4)
```

在测试的时候，数据将会被分类入欧式距离最小的中心点坐标。

输入：数据集data，类聚个数K，训练集与测试集的比例ratio（默认为4）

输出：plt图展示。


