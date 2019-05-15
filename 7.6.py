# 
# Create a class Rectangle. The class has attributes __length and __width, each of
# which defaults to 1. It has methods that calculate the perimeter and the area of the rectangle. It
# has set and get methods for both __length and __width. The set methods should verify that
# __length and __width are each floating-point numbers larger than 0.0 and less than 20.0. Write
# a driver program to test the class

class Rectangle:

    def __init__(self, lenght = 1, width = 1):


        self.lenght = lenght
        self.width = width


        self.perimeter(self.lenght, self.width)
        self.area(self.lenght, self.width)
        print("Perimeter: %f" % self.P)
        print("Area: %f" % self.A)


    def perimeter(self, l, w):

        P = 2*(l + w)
        print("Perimeter: %f" % P)
        return P


    def area(self, l , w):

        A = l*w
        self.A = A
        print("Area: %f" % A)
        return A

    def getParameter(self):
        return (self.__lenght, self.__width)

    def setParameter(self, l, w):

        if 0.0 < float(l) < 20.0:
            if 0.0 < float(w) < 20.0:
                self.__lenght = l
                self.__lenght = w

            else:
                raise ValueError("Invalid value entered %.2f" %(w))

        else:
            raise ValueError("Invalid value entered %.2f" %(l))

x = Rectangle(1,2)
