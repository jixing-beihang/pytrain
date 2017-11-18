from collections import namedtuple, deque, OrderedDict, defaultdict, Counter

# namedtuple 类似于创建一个类
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(2, 3, 4)
print(c.x, c.y, c.r)

# deque 双向列表
q = deque(['a', 'b', 'c'])
q.append('x')
print(q)
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# defaultdic 有默认值字典
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值

# OrderDict 有序字典
d = dict()
d['z'] = 1
d['y'] = 2
d['x'] = 3
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(d, od)

# 计数器Counter,是一个字典
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
