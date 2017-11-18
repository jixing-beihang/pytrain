#  斐波那契数列
# def fibs(num):
#     result = [0, 1]
#     for i in range(num - 2):
#         print(i)
#         result.append(result[-2] + result[-1])
#     return result
# print(fibs(3))
# print(fibs(2))

# 函数定义
# def init(data):
#     data['first'] = {}
#     data['middle'] = {}
#     data['last'] = {}
#     print('初始化完成:', data)
#
#
# def lookup(data, label, name):
#     return data[label].get(name)
#
#
# def stor(data, *full_names):  # 通过‘*’收集位置参数，通过‘**’收集关键字参数
#     print('传入的值：', full_names)
#     for full_name in full_names:
#         print('处理的值：', full_name)
#         names = full_name.split()
#         if len(names) == 2: names.insert(1, '')
#         print('格式化名字：', names)
#         labels = 'first', 'middle', 'last'
#         dic = dict(zip(labels, names))
#         print(dic)
#         for label, name in dic.items():
#             people = lookup(data, label, name)
#             if people:
#                 people = people.append(full_name)
#             else:
#                 data[label][name] = [full_name]
#                 print('数据库：', data)
#
#
# MyNames = {}
# init(MyNames)
# # stor(MyNames, 'Magum Lie Hetland')
# # print(lookup(MyNames, 'middle', 'Lie'))
#
# stor(MyNames, 'Luke Skywalker', 'Anakin Skywalker')
# print(lookup(MyNames, 'last', 'Skywalker'))

# practice
def story(**kwds):
    return 'Once upon a time, there is %(job)s called %(name)s' % kwds


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, step
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


params = {'job': 'language', 'name': 'Python'}
print(story(job='king', name='Gumby'), story(name='Sir Robin', job='brave knight'), story(**params))

print(power(2,3),power(3,2),power(x=2,y=3),power(3,3,'Hello World'))

print(interval(1,5))

def search(sequence,number,lower=0,upper=None):
    if upper is None:upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)

sequence = [1,3,5,7,8,9]
print(sequence.index(8))
print(search(sequence,8))