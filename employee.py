class employee:

    def __init__(self, first, last):

        self.firstname = first
        self.lastname = last

    def __str__(self):

        return("%s %s" % (self.firstname, self.lastname))

class HourlyWorker(employee):

    def __init__(self, first, last, initHour, initWage):

        employee.__init__(self,first, last)
        self.Hour = float(initHour)
        self.Wage = float(initWage)

    def getPay(self):

        return(self.Hour * self.Wage)

    def __str__(self):

        print(" %s is an hourly worker with pay of $%.2f" %(employee.__str__(self), self.getPay()))

hourly = HourlyWorker("Jonathan", "Ifegunni", 40.0, 10.00)

print(hourly.__str__())
