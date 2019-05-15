# Create a class called RationalNumber for performing arithmetic with fractions. Write a
# driver program to test your class.
# Use integer variables to represent the data of the class—the numerator and the denominator.
# Provide a constructor that enables an object of this class to be initialized when it is declared. The
# constructor should contain default values, in case no initializers are provided, and should store the
# fraction in reduced form (i.e., the fraction
# 2/4
# would be stored in the object as 1 in the numerator and 2 in the denominator). Provide methods for
# each of the following:
# a) Adding two RationalNumbers. The result should be stored in reduced form.
# b) Subtracting two RationalNumbers. The result should be stored in reduced form.
# c) Multiplying two RationalNumbers. The result should be stored in reduced form.
# d) Dividing two RationalNumbers. The result should be stored in reduced form.
# e) Printing RationalNumbers in the form a/b, where a is the numerator and b is the
# denominator.
# f) Printing RationalNumbers in floating-point format.



class RationalNumber:

    def __init__(self, num1 = 0, denum1 = 1, num2 = 0, denum2 = 1):

        num1 = int(input("enter the numerator of the first fraction: "))
        denum1 = int(input("enter the denominator of the first fraction: "))
        num2 = int(input("enter the numerator of the second fraction: "))
        denum2 = int(input("enter the denominator of the second fraction: "))

        self.num1 = num1
        self.denum1 = denum1
        self.num2 = num2
        self.denum2 = denum2

        self.addRationalNumbers(self.num1, self.num2, self.denum1, self.denum2)
        self.subRationalNumbers(self.num1, self.num2, self.denum1, self.denum2)
        self.mulRationalNumber(self.num1, self.num2, self.denum1, self.denum2)
        self.divRationalNumber(self.num1, self.num2, self.denum1, self.denum2)
        self.fracRationalNumber(self.numerator, self.denominator, self.SubNumerator, self.SubDenominator, self.mulNumerator, self.mulDenominator, self.divNumerator, self.divDenominator )
        self.floatingRationalNumber(self.numerator, self.denominator, self.SubNumerator, self.SubDenominator, self.mulNumerator, self.mulDenominator, self.divNumerator, self.divDenominator )




    def addRationalNumbers(self, numerator1, numerator2, denominator1, denominator2):

        self.numerator = (self.num1 * self.denum2) + (self.num2 * self.denum1)

        self.denominator = (self.denum1 * self.denum2)

        if self.numerator == self.denominator:
            self.numerator = int(1)
            self.denominator = int(1)

        else:
            for i in range(2, 11):
                while self.numerator % i == 0 and self.denominator % i == 0:
                    self.numerator = self.numerator // i
                    self.denominator = self.denominator // i
            return(self.numerator, self.denominator)

    def subRationalNumbers(self, numerator1, numerator2, denominator1, denominator2):
        self.SubNumerator = (self.num1 * self.denum2) - (self.num2 * self.denum1)

        self.SubDenominator = (self.denum1 * self.denum2)

        if self.SubNumerator == self.SubDenominator:
            self.SubNumerator = 1
            self.SubDenominator = 1

        else:
            for i in range(2, 11):
                while self.SubNumerator % i == 0 and self.SubDenominator % i == 0:
                    self.SubNumerator = self.SubNumerator // i
                    self.SubDenominator = self.SubDenominator // i
            return(self.SubNumerator, self.SubDenominator)


    def mulRationalNumber(self, numerator1, numerator2, denominator1, denominator2):
        self.mulNumerator = (self.num1 * self.num2)

        self.mulDenominator = (self.denum1 * self.denum2)

        if self.mulNumerator == self.mulDenominator:
            self.mulNumerator = 1
            self.mulDenominator = 1

        else:
            for i in range(2, 11):
                while self.mulNumerator % i == 0 and self.mulDenominator % i == 0:
                    self.mulNumerator = self.mulNumerator // i
                    self.mulDenominator = self.mulDenominator // i
            return(self.mulNumerator, self.mulDenominator)

    def divRationalNumber(self, numerator1, numerator2, denominator1, denominator2):
        self.divNumerator = (self.num1 * self.denum2)

        self.divDenominator = (self.num2 * self.denum1)

        if self.divNumerator == self.divDenominator:
            self.divNumerator = 1
            self.divDenominator = 1

        else:
            for i in range(2, 11):
                while self.divNumerator % i == 0 and self.divDenominator % i == 0:
                    self.divNumerator = self.divNumerator // i
                    self.divDenominator = self.divDenominator // i
            return(self.divNumerator, self.divDenominator)


    def fracRationalNumber(self, num1, denum1, num2, denum2, num3, denum3, num4, denum4):
        print("The addition of the 2 fraction is:", "%.i/%.i" %(num1, denum1))
        print("The subraction of the 2 fraction is:", "%.i/%.i" %(num2, denum2))
        print("The multiplication of the 2 fraction is:", "%.i/%.i" %(num3, denum3))
        print("The division of the 2 fraction is:", "%.i/%.i" %(num4, denum4))


    def floatingRationalNumber(self, num1, denum1, num2, denum2, num3, denum3, num4, denum4):
        print("The addition of the 2 fraction is:", "%.2f" %(num1/denum1))
        print("The subraction of the 2 fraction is:", "%.2f" %(num2/denum2))
        print("The multiplication of the 2 fraction is:", "%.2f" %(num3/denum3))
        print("The division of the 2 fraction is:", "%.2f" %(num4/denum4))


x = RationalNumber()
