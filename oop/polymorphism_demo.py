import math

class Shape:
    def area(self):
        # Raise a NotImplementedError to enforce method overriding in subclasses
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Calculate the area of the rectangle
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculate the area of the circle using pi * r^2
        return math.pi * (self.radius ** 2)