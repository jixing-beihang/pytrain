'''
优点：
1、装饰器模式是继承方式的一个替代方案，可以轻量级的扩展被装饰对象的功能；
2、Python的装饰器模式是实现AOP的一种方式，便于相同操作位于不同调用位置的统一管理。
应用场景：
1、需要扩展、增强或者减弱一个类的功能，如本例。
装饰器模式的缺点
1、多层装饰器的调试和维护有比较大的困难。
'''
from _datetime import datetime


class LogManager():
    @staticmethod
    def log(func):
        def wrapper(*args):
            print('call %s' % func.__name__)
            return func(*args)

        return wrapper


@LogManager.log
class Beverage(object):
    _name = ''
    _price = 0.0
    _type = 'Beverage'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price


class Coke(Beverage):
    def __init__(self):
        self._name = 'coke'
        self._price = 4.0


class Milk(Beverage):
    def __init__(self):
        self._name = 'milk'
        self._price = 5.0


class DrinkDecorator(object):
    def getName(self):
        pass

    def getPrice(self):
        pass


class IceDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.name + 'ice'

    def getPrice(self):
        return self.beverage.price + 0.3


class SugarDecorator(DrinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.name + 'sugar'

    def getPrice(self):
        return self.beverage.price + 0.5


def log(fun):
    def wrapper(*args, **kwargs):
        print('call %s()' % fun.__name__)
        return fun(*args, **kwargs)

    return wrapper


@log
def now():
    print(datetime.now().strftime('%Y%m%d %H:%M:%S'))


if __name__ == '__main__':
    coke_cola = Coke()
    print('Name:%s' % coke_cola.name)
    print('Price:%s' % coke_cola.price)

    ice_coke = IceDecorator(coke_cola)
    print('Name:%s' % ice_coke.getName())
    print('Price:%s' % ice_coke.getPrice())

    now()
