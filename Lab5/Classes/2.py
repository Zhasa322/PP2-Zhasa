class Shape():
    def __init__(self):
        self.int=int()

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = int(input())

    def area(self):
        print(self.length * self.length)


aSquare = Square(Shape)
aSquare.area()      