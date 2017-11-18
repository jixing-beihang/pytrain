import math as foobar
from math import sqrt
print(foobar.pi)
# 赋值:序列解包，链式赋值，增量赋值
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# key,value = phonebook.popitem() # 多个值同时赋值
# print(key,value)

x = y = phonebook
print(x,y)

a = 3
a *= 2
print(a)
# elif 语句
# num = int(input("enter a number:"))
# zero = 0
# if num > zero:
#     print('this is positive')
# elif num < zero:
#     print('this is negative')
# else:
#     print('this is zero')
# if 嵌套
# name = input("enter a name:")
# if name.endswith('Gumby'):
#     if name.startswith('Mr.'):
#         print('Hello Mr. Gumby -- if')
#     elif name.startswith('Mrs.'):
#         print('Hello Mrs. Gumby -- elif')
#     else:
#         print('Hello Gumby -- else')
# else:
#     print('Hello stranger. -- else')

# 断言 assert，用于调试
age = -1
# assert 0 < age < 100 ,'age must be positive'

# 循环 while
# x = 1
# while x <= 100:
#     print(x)
#     x += 1

# name = ''
# while not name.strip():
#     name = input('enter a name:')
# print('Hello %s.' % name)

# for 循环
# for cal in range(1,10):
#     print(cal)

# for 循环遍历字典
for key,value in phonebook.items():
    print("%s's phone number is  %s" % (key,value))

# 迭代工具 zip,enumerate
# lis = zip(range(5),range(5000))
# print(lis)

# while True/break，当不输入字符时就退出
# while True:
#     word = input('enter a word:')
#     if not word:break
#     print('the word is %s' % word)

# for循环在break的时候执行else部分
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find")

