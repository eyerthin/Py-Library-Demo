这个模块提供了堆队列算法的实现，也称为优先队列算法。

堆是一个二叉树，它的每个父节点的值都只会小于或等于所有孩子节点（的值）。 它使用了数组来实现：从零开始计数，对于所有的 *k* ，都有 `heap[k] <= heap[2*k+1]` 和 `heap[k] <= heap[2*k+2]`。 为了便于比较，不存在的元素被认为是无限大。 堆最有趣的特性在于最小的元素总是在根结点：`heap[0]`。



要创建一个堆，可以使用list来初始化为 `[]` ，或者你可以通过一个函数 [`heapify()`](https://docs.python.org/zh-cn/3.10/library/heapq.html#heapq.heapify) ，来把一个list转换成堆。

```python
from heapq import *

# 将item的值加入heap中，保持堆的不变性。
heappush(heap, item)

# 弹出并返回heap的最小的元素，保持堆的不变性。
heappop(heap)

# heappush() + heappop()，更有效率。
heappushpop(heap, item)

# heappop() + heappush(),更有效率。
heapreplace()

# 将list x转换为堆。
heapify(x)

# 从iterable所定义的数据集中，返回前n个最大元素组成的列表。key是从iterable中提取比较键的参数。
# 等价于sorted(iterable, key=key, reverse=True)[:n]
nlargest(n, iterable, key=None)
# 最小
nsmallest(n, iterable, key=None)

# 将多个已排序的输入合并为一个已排序的输出。
# key同nlargest()和nsmallest()。
# reverse为bool，True为逆序合并。 
merge(*iterables, key=None, reverse=False)
```