'''
桥梁模式优点：
1、抽象角色与实现角色相分离，二者可以独立设计，不受约束；
2、扩展性强：抽象角色和实现角色可以非常灵活地扩展。
应用场景：
1、不适用继承或者原继承关系中抽象类可能频繁变动的情况，可以将原类进行拆分，拆成实现化角色和抽象化角色。例如本例中，若将形状、粗细、绘画样式等属于汇集在一个类中，一旦抽象类中有所变动，将造成巨大的风险；
2、重用性比较大的场景。比如开关控制逻辑的程序，开关就是抽象化角色，开关的形式有很多种，操作的实现化角色也有很多种，采用桥梁模式，（如当前例子）开关即可进行复用，整体会将设计的粒度减小。
桥梁模式缺点
1、增加对系统理解的难度。

'''


class Shape(object):
    name = ""
    param = ""

    def __init__(self, *param):
        pass

    def getName(self):
        return self.name

    def getParam(self):
        return self.name, self.param


class Pen(object):
    shape = ""
    type = ""

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass


class Rectangle(Shape):
    def __init__(self, long, width):
        super().__init__(long, width)
        self.name = "Rectangle"
        self.param = "Long:%s Width:%s" % (long, width)
        print("Create a rectangle:%s" % self.param)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.name = "Circle"
        self.param = "Radius:%s" % radius
        print("Create a circle:%s" % self.param)


class NormalPen(Pen):
    def __init__(self, shape):
        super().__init__(shape)
        self.type = "Normal Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


class BrushPen(Pen):
    def __init__(self, shape):
        super().__init__(shape)
        self.type = "Brush Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


if __name__ == "__main__":
    normal_pen = NormalPen(Rectangle("20cm", "10cm"))
    brush_pen = BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()
