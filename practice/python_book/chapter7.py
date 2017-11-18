# 类的命名空间
class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1  # 类的所有实例对象都可以访问


m1 = MemberCounter()
m1.init()
m1.members = 'TWO'
print(m1.members)
m2 = MemberCounter()
m2.init()
print(m2.members)


# 超类和继承
class Filter():
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    super
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1, 2, 3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'egg']))
# 查看父类，issubclass(child，parent), chileClass.__bases__，instance.__class__
print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))
print(SPAMFilter.__bases__)
print(s.__class__)
print(s.__dict__)
print(SPAMFilter.__dict__)


class Calculator():
    def calcaulate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi my value is ', self.value)


class TalkingCalculate(Calculator, Talker):
    pass

tc = TalkingCalculate()
tc.calcaulate('1+2*3')
tc.talk()

# Talker.talk('7')