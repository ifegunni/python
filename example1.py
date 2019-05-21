class phoneNumber:

     def __init__(self, number):
         self.areaCode = number[0:3]
         self.exchange = number[3:6]
         self.line = number[6:10]

     def __str__(self):
         return("(%s) %s-%s" %(self.areaCode, self.exchange, self.line))

def test():
    newNumber = input("Enter your phone number: ")
    phone = phoneNumber(newNumber)
    print("The phone number is:", phone)

if __name__ == "__main__":
    test()
