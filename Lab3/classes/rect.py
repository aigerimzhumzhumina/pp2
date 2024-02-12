class Shape:
    def __init__(self, length):
        self.length = length
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
    def area(self):
        return self.length * self.width 
area = Rectangle(5, 10)
print(area.area())