class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0

class Square(Shape):
     
    def area(self):
        return self.length ** 2
areashape = Shape(0)  
areasquare = Square(5)

print(areashape.area())  
print(areasquare.area())  