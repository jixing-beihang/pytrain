#  索引，分片，序列相加，乘法
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[1:3])
print(numbers[-3:-1])
print(numbers[-3:0])
print(numbers[-3:])
print(numbers[:3])
print("ji" * 3)
# 成员in，最大，最小，长度
users = ['mlh','foo','bar']
# 列表方法 append
users.append('foo')
print(users)
# 列表方法 count,index,in;max,min,len
print(users.count('foo'))
print(users.index('foo'))
print('foo' in users)
print(min(numbers),max(numbers),len(users))
# 列表赋值
x = [1,1,1]
x[1] = 2
print(x)
# 分片赋值
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)
name[1:] = list('ython')
print(name)
# 分片赋值和分片删除
numbers[1:1] = [3,2,1]
print(numbers)
numbers[1:4] = []
print(numbers)
# 列表方法 extend,insert,pop,remove,reverse&reversed
a = [1,2,3]
b = [4,5,6]
a.extend(b)
a.insert(2,'xing')
print(a)
a.pop(0)
print(a)
a.remove('xing')
print(a)
a.reverse()
rev_a = list(reversed(a))
# rev_a = reversed(a)
print(a)
print(rev_a)
# 列表方法 sort&sorted
x = [4,6,2,1,7,9]
y = x[:]
y.sort(reverse=True)
print(x)
print(y)
x = [4,6,2,1,7,9]
y = sorted(x)
y.reverse()
print(x)
print(y)
# 元组,tuple
tup = 42,
print(tup)
tupl = tuple([1,2,3,4])
print(tupl)
print(tupl[:2])