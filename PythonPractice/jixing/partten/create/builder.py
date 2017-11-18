'''
优点：
1、封装性好，用户可以不知道对象的内部构造和细节，就可以直接建造对象；
2、系统扩展容易；
3、建造者模式易于使用，非常灵活。在构造性的场景中很容易实现“流水线”；
4、便于控制细节。
使用场景：
1、目标对象由组件构成的场景中，很适合建造者模式。例如，在一款赛车游戏中，车辆生成时，需要根据级别、环境等，选择轮胎、悬挂、骨架等部件，构造一辆“赛车”；
2、在具体的场景中，对象内部接口需要根据不同的参数而调用顺序有所不同时，可以使用建造者模式。例如：一个植物养殖器系统，
    对于某些不同的植物，浇水、施加肥料的顺序要求可能会不同，因而可以在Director中维护一个类似于队列的结构，在实例化时作为参数代入到具体建造者中。
建造者模式的缺点
1、“加工工艺”对用户不透明。（封装的两面性）
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


class Order(object):
    burger = ''
    snack = ''
    beverage = ''

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print('Burger:%s' % self.burger.name)
        print('Snack:%s' % self.snack.name)
        print('Beverage:%s' % self.beverage.name)


class OrderBuilder(object):
    bBurger = ''
    bSnack = ''
    bBeverage = ''

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return Order(self)


class OrderDirector(object):
    order_builder = ''

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


if __name__ == '__main__':
    # order_builder = OrderBuilder()
    # order_builder.addBurger(SpricyBurger())
    # order_builder.addSnack(Chips())
    # order_builder.addBeverage(Milk())
    # order1 = order_builder.build()
    # order1.show()

    order_director = OrderDirector(OrderBuilder())
    order = order_director.createOrder(CheeseBurger(), ChickenWings(), Coke())
    order.show()
