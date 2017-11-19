# # 枚举类型，实现迭代iteration
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
#
# # 列表推导式,if进行判断
# lizt = [x * y for x in range(1, 11) for y in (11, 20) if x % 2 == 0]
# print(lizt)
#
# import os
#
# print([d for d in os.listdir('.')])
# # 列表推导式,if进行判断
# L = ['Hello', 'World', 18, 'Apple', None]
# print([d.lower() for d in L if isinstance(d,str)])
#
# # 生成器 generator
# g = (x*x for x in range(1,11))
# for n in g:
#     print(n)

# 斐波那契数列 1 1 2 3 5 8 ，递归法
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
#
#
# print(fib(6))
#
#
# # 斐波那契数列 1 1 2 3 5 8，迭代法
# def fibo(n):
#     a, b, i = 1, 1, 2  # a,b位fib(1),fib(2)
#     while i < n:
#         a, b = b, a + b
#         i += 1
#     return b
#
#
# print(fibo(6))
#
#
# # 斐波那契数列 1 1 2 3 5 8，迭代法,使用生成器
# def fibon(n):
#     a, b, i = 1, 1, 2  # a,b位fib(1),fib(2)
#     while i < n:
#         a, b = b, a + b
#         i += 1
#     yield b
#
#
# for num in fibon(6):
#     print(num)
# from functools import reduce
#
#
# def normalize(name):
#     return name[0].upper() + name[1:].lower()
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#
#
# def prod(L):
#     return reduce(lambda x, y: x * y, L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
import time


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s' % func.__name__)
        return func(*args, **kwargs)

    return wrapper

# log 装饰器需要在调用前定义
@log
def now():
    print(time.strftime('%Y%m%d%H%M%S', time.localtime()))  # strftime 格式化函数，年月日时分秒格式


# 按格式打印时间
now()

# 偏函数 partial
import functools

int10 = functools.partial(int, base=10)
int2 = functools.partial(int, base=2)  # 将二进制数转换为十进制
int8 = functools.partial(int, base=8)  # 将八进制数转换为十进制
int16 = functools.partial(int, base=16)  # 将十六进制数转换为十进制
print(int10('8'))
print(int2('10010'))
print(int8('777'))
print(int16('fff'))
