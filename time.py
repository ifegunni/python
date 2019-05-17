class Time:

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __setattr__(self, name, value):
        name = str(name)

        if name =="hour":
            if 0 <= value < 24:
                self.__dict__["_hour"] = value
            else:
                raise ValueError("Invalid hour value: %d" % value)
        elif name == "minute" or name == "second":
            if 0 <= value < 60:
                self.__dict__["_" + name] = value
            else:
                raise ValueError("Invalid %s value: %d" % (name, value))

        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == "hour":
            return self._hour
        elif name == "minute":
            return self._minute
        elif name == "second":
            return self._second
        else:
            raise AttributeError(name)

    def __str__(self):
        return("%.2d:%.2d:%.2d" % (self._hour, self._minute, self._second))

time1 = Time(4, 27, 19)
print(time1)
time1.hour = 16
print(time1)
time1.__setattr__(hour, 20)
print(time1)
