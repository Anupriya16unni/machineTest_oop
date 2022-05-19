from turtle import width


class Area:
    breadth = 0
    length = 0

class Rectangle(Area):

    def __init__(self, b, l):
        self.breadth = b
        self.length = l
 
    def calculateArea(self):
        print("Area of the Rectangle is : ", self.breadth*self.length)

class Circle(Area):
 
    def __init__(self, l):
        self.length = l
 
    def calculateArea(self):
        print("Area of the circle is : ", 3.14*((self.length/2)*(self.length/2)))

rectangle = Rectangle(10, 20)
rectangle.calculateArea()

circle = Circle(10)
circle.calculateArea()