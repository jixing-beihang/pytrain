from copy import deepcopy
# 字典初始化
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 创建字典 dict
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
print(d['name'])
# 字典操作
# people = {'Alice': {'phone': '2341', 'address': 'Street 3'},
#           'Beth': {'phone': '9102', 'address': 'Bar 42'},
#           'Cecil': {'phone': '3258', 'address': 'Avenue 90'}}
# labels = {'phone': 'phone number', 'address': 'address'}
#
# name = input('name:')
# request = input('p or a?')
#
# if request == 'p': key = 'phone'
# if request == 'a': key = 'address'
#
# if name in people:
#     print("%s's %s is %s." % (name, labels[key], people[name][key]))

# 字符串格式化
print("Beth's phone number is %(Beth)s." % phonebook)
# 字典方法 clear,copy,get,setdefault,keys,values,items,update
# print(d.clear())
# 字典方法，copy浅复制，原位修改
# c = d.copy()
c = deepcopy(d)
c['name'] = 'Admin'
print(c.get('name'))
print(c.keys())
print(c.values())
print(c.items())
print(c.setdefault('name'))
print(c.setdefault('sex','male'))
print(c)
print(d)

e = {'name':'GUI'}
d.update(e)
print(d)