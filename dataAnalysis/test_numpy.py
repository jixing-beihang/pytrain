import os

import numpy as np

path = os.path.join(os.path.abspath('.'),'data.txt')
print(path)
# 从文件中读取数组 genfromtxt
world_alcohol = np.genfromtxt(path, delimiter=',', dtype=int)
print(type(world_alcohol))
print(world_alcohol)
# print(help(np.genfromtxt))

vector = np.array([1,2,3,4.0])
matrix = np.array([[1,2,3],[4,5,6]])
# 查看结构 类型 维度 数量，shape dtype ndim size
print(vector.shape)
print(vector.dtype)
print(vector.ndim)
print(vector.size)
print(matrix.shape)
print(matrix.dtype)
print(matrix.ndim)
print(matrix.size)
# 根据条件获取 == | &
vector5 = vector * 5
print(vector5)
equal_to_ten = (vector5 == 10)
equal_to_ten_and_five = (vector5 == 10) | (vector5 == 5)

print(equal_to_ten)
print(equal_to_ten_and_five)
# 类型转换 astype
vector = vector.astype(str)
print(vector)
print(vector.dtype)
# 数组求和 sum, axis=1表示按照 x轴方向求和，axis=0表示按照y轴方向求和
matrix3 = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print(matrix3)
print(matrix3.sum())
print(matrix3.sum(axis=1))
print(matrix3.sum(axis=0))

# 常用函数 reshape zeros ones range rondom
print(np.arange(0,15,1).reshape(3,5))
print(np.zeros((3,3)))
print(np.ones((3,3)))
print(np.arange(0,10,2,dtype=int))
print(np.random.random((2,3)))

# ndarray 相减 乘方 开方 e次方 向下取整 转置等运算 - ** sqrt exp floor T
a = np.array([10,20,30,40])
b = np.array([4])
print(a-b)
print(a**2)
print(np.sqrt(a))
print(np.exp(a))
print(np.floor(10*np.random.random((2,2))))
# 转置
print(matrix)
print(matrix.shape)
c = matrix.T
print(c)
print(c.shape)
d = a.resize(1,4)
print(d)

# 矩阵运算 逐个相乘 矩阵相乘
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print(A)
print(B)
print(A*B)
print(np.dot(A,B))

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(a)
print(b)
# 矩阵的合并 vstack hstack
print(np.vstack((a,b)))
print(np.hstack((a,b)))
# 矩阵的拆分 vsplit hsplit
print(np.vsplit(a,2))
print(np.hsplit(a,2))

# 复制 = view copy
a = np.arange(12)
b = a
print(b is a)
print(a.shape)
print(b.shape)
b.shape = (3,4)
print(a.shape)
print(b.shape)
# view
a = np.arange(12)
c = a.view()
print(c is a)
c.shape = 2,6
c[0,0] = 999
print(a)
print(c)
# copy
a = np.arange(12)
c = a.copy()
print(c is a)
c.shape = 2,6
c[0,0] = 999
print(a)
print(c)