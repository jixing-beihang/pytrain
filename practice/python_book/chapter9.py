class Bird():
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry == True:
            print('Ah aaaaa')
            self.hungry = False
        else:
            print('No thanks...')


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super().__init__()
        self.song = 'Squak!'

    def sing(self):
        print(self.song)


sb = SongBird()
sb.sing()
sb.eat()
sb.eat()


class Rectangle():
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)


r = Rectangle()
r.width = 100
r.height = 5
print(r.size)
