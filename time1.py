class time:

    def __init__(self):

        self._hour = 0
        self._minute = 0
        self._second = 0

    def setTime( self, hour, minute, second ):

        self.setHour( hour )
        self.setMinute( minute )
        self.setSecond( second )

    def setHour (self, hour):

        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError("Invalid hour value: %d" % hour)

    def setMinute (self, minute):

        if 0 <= minute < 60:
            self._minute = minute
        else:
            raise ValueError("Invalid minute value: %d" % minute)

    def setSecond (self, second):

        if 0 <= second < 60:
            self._second = second
        else:
            raise ValueError("Invalid second value: %d" % second)

    def getHour( self ):

        return self._hour

    def getMinute( self ):

        return self._minute

    def getSecond( self ):

        return self._second

    def printMilitary(self):
        print ("%.2d:%.2d:%.2d"% (self._hour, self._minute, self._second))

    def printStandard(self):
        standardTime = " "

        if self.hour == 0 or self.hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % (self.hour % 12)

        standardTime += "%.2d:%.2d" % (self.minute, self.second)

        if self.hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"

        print(standardTime)

xx = time()
xx.setTime(20,10,10)
print(xx.printMilitary())
