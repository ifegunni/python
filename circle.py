import math

class point():

    def __init__(self, xValue = 0, yValue = 0):

        self.x = xValue
        self.y = yValue

class circle(point):

    def __init__(self, x = 0, y = 0, radiusValue = 0.0):

        point.__init__(x, y)
        self.radius = float(radiusValue)

    def Area(self):
        return math.pi * self.radius **2

# print("Point bases:", point.__bases__)
# print("Point bases:", circle.__bases__)

point = point(30, 50)
circle = circle(120, 89, 2.7)
print(circle.Area())
