#
# Create a class called Complex for performing arithmetic with complex numbers. Write a
# driver program to test your class.
# Complex numbers have the form
# realPart + imaginaryPart * i
# where i is
# Use floating-point numbers to represent the data of the class. Provide a constructor that enables an
# object of this class to be initialized when it is created. The constructor should contain default values
# in case no initializers are provided. Provide methods for each of the following:
# a) Adding two ComplexNumbers: The real parts are added to form the real part of the result, and the imaginary parts are added to form the imaginary part of the result.
# b) Subtracting two ComplexNumbers: The real part of the right operand is subtracted
# from the real part of the left operand to form the real part of the result, and the imaginary
# part of the right operand is subtracted from the imaginary part of the left operand to form
# the imaginary part of the result.
# c) Printing ComplexNumbers in the form (a, b), where a is the real part and b is the
# imaginary part

class Complex:

    def __init__(self):

        self.real1 = float(input("Enter the real part of the first complex number: "))
        self.imag1 = float(input("Enter the imaginary part of the first complex number: "))

        self.real2 = float(input("Enter the real part of the second complex number: "))
        self.imag2 = float(input("Enter the imaginary part of the second complex number: "))

        self.ComplexNumber()

    def ComplexNumber(self):
        self.addComplexNumber(self.real1, self.real2, self.imag1, self.imag2)
        self.subComplexNumber(self.real1, self.real2, self.imag1, self.imag2)


    def addComplexNumber(self, real1, real2, imaginary1, imaginary2):
        addRealPart = self.real1 + self.real2
        addImagPart = self.imag1 + self.imag2
        print("The sum of the complex numbers is:", (addRealPart, addImagPart))

    def subComplexNumber(self, real1, real2, imaginary1, imaginary2):
        subRealPart = self.real1 - self.real2
        subImagPart = self.imag1 - self.imag2
        print("The difference of the complex numbers is:", (subRealPart, subImagPart))


x = Complex()
