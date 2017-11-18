'''
工厂模式、抽象工厂模式的优点：
1、工厂模式巨有非常好的封装性，代码结构清晰；在抽象工厂模式中，其结构还可以随着需要进行更深或者更浅的抽象层级调整，非常灵活；
2、屏蔽产品类，使产品的被使用业务场景和产品的功能细节可以分而开发进行，是比较典型的解耦框架。
工厂模式、抽象工厂模式的使用场景：
1、当系统实例要求比较灵活和可扩展时，可以考虑工厂模式或者抽象工厂模式实现。比如，
在通信系统中，高层通信协议会很多样化，同时，上层协议依赖于下层协议，那么就可以对应建立对应层级的抽象工厂，根据不同的“产品需求”去生产定制的实例。
工厂类模式的不足
1、工厂模式相对于直接生成实例过程要复杂一些，所以，在小项目中，可以不使用工厂模式；
2、抽象工厂模式中，产品类的扩展比较麻烦。毕竟，每一个工厂对应每一类产品，产品扩展，就意味着相应的抽象工厂也要扩展。
'''

class Burger(object):
    _name = ''
    _price = ''

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


class CheeseBurger(Burger):
    def __init__(self):
        self._name = 'cheese burger'
        self._price = 10.0


class SpricyBurger(Burger):
    def __init__(self):
        self._name = 'spricy burger'
        self._price = 15.0


class Snack(object):
    _name = ''
    _price = 0.0
    _type = 'Snack'

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


class Chips(Snack):
    def __init__(self):
        self._name = 'chips'
        self._price = 6.0


class ChickenWings(Snack):
    def __init__(self):
        self._name = 'chicken wings'
        self._price = 12.0


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


# 抽象工厂类
class Factory():
    type = ''

    def createFood(self, foodClass):
        print(self.type, 'factory produce a instance')
        foodIns = foodClass()
        return foodIns


# 具体工厂类
class BurgerFactory(Factory):
    def __init__(self):
        self.type = 'Burger'


class SnackFactory(Factory):
    def __init__(self):
        self.type = 'Snack'


class BeverageFactory(Factory):
    def __init__(self):
        self.type = 'Beverage'


# 简单工厂方法类
class SimpleFactory():
    @classmethod
    def createFood(cls, foodClass):
        print('SimpleFactory factory produce a instance')
        foodIns = foodClass()
        return foodIns


if __name__ == '__main__':
    burger_factory = BurgerFactory()
    snack_factory = SnackFactory()
    beverage_factory = BeverageFactory()

    cheese_burger = burger_factory.createFood(CheeseBurger)
    print(cheese_burger.name, cheese_burger.price)

    chicken_wings = snack_factory.createFood(ChickenWings)
    print(chicken_wings.name, chicken_wings.price)

    coke_drink = beverage_factory.createFood(Coke)
    print(coke_drink.name, coke_drink.price)

    milk_drink = SimpleFactory.createFood(Milk)
    print(milk_drink.name, milk_drink.price)
