import math
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def show(self):
        print(self.x, self.y)
    def move(self, x1, y1):
        self.x = x1 
        self.y = y1 
    def dist(self, otherpoint):
        distance = math.sqrt((self.x-otherpoint.x)**2 + (self.y-otherpoint.y)**2)
        return distance
point1 = Point(2,5)
point2 = Point(3,4)
point1.show()
point2.show()
point1.move(1,2)
point1.show()
distance = point1.dist(point2) 
print(distance)