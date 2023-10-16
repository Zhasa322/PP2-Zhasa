class point():
    def __init__(self, point1, point2):
        self.point1=point1
        self.point2=point2
    def show(self):
        print(self.point1)
        print(self.point2)
    def move(self):
        self.point1=int(input())
        self.point2=int(input())
    def dist(self):
        print(self.point1-self.point2)
point1=int(input())
point2=int(input())
pnt=point(point1, point2)
pnt.show()
pnt.move()
pnt.dist()