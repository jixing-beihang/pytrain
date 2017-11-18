# class Student(object):
#     pass

class Student(object):
    __slots__ = ('name', '_score', '_birth')  # __slots__定义的属性只在当前类起作用，在子类中不起作用

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a numbr')
        elif value < 0 or value > 100:
            raise ValueError('Between 0 ~ 100')
        else:
            self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


class GraduateStudent(Student):
    __slots__ = ('name', 'age', 'sex')  # 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
    pass


s = Student()
s.name = 'apache'
s.set_score(90)
s.birth = 1990
# s.sex = 'male' # 未在 __slots__中定义的实例属性不能赋值
print(s.name, s.age, s._score, s.birth, s.age)

g = GraduateStudent()
g.sex = 'male'
# g.score = 90
print(g.sex)


# @property 属性,实现getter,setter
class Screen(object):
    def __init__(self):
        _width = 0
        _height = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._hetght

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# 枚举 enumeration
# from enum import Enum
# Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(Month.Jan)
#
# for name,member in Month._member_map_.items():
#     print(name,'=>',member,',',member.value)

# 操作文件和目录，os,sys
import os
print(os.name)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'),'test.sh'))
print(os.path.splitext('/PythonPractice/jixing/test.sh'))
print(os.path.split('/PythonPractice/jixing/test.sh'))

# 序列化 pickle
# import pickle
# d = {'name':'Bob','age':27,'score':88}
# print(pickle.dumps(d))  # pickle.dumps()方法把任意对象序列化成一个bytes
# f = open('dump.txt','wb',1)
# # pickle.dump(d,f) # pickle.dump()直接把对象序列化后写入一个file-like Object
# f.close()

# fread = open('dump.txt','rb',1)
# dict_read = pickle.load(fread)
# fread.close()
# print(dict_read)
