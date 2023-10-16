class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0
    
class rectangle(Shape):
    def __init__(self, width, length):
        
        self.width=width
        self.length=length
    def area(self):
        return self.width * self.length

width = int(input())
length = int(input())
rect1 = rectangle(width, length)
print(rect1.area())