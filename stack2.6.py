class Stack:

    def __init__(self):
        self.item = []
        self.min = []

    def push(self, item):
        self.item.append(item)
        if self.isEmpty():
            self.min.append(item)
        elif item <= self.min[-1]:
                self.min.append(item)

    def pop(self):
        if self.item[-1] == self.min[-1]:
            self.min.pop()
            return self.item.pop()
        else:
            return self.item.pop()

    def minimum(self):
        return self.min[-1]

    def __str__(self):
        return str(self.item)

    def isEmpty(self):
        return self.min == []

s = Stack()
s.push(2)
print(s)
print(s.minimum())
s.push(5)
print(s)
print(s.minimum())
s.push(1)
print(s)
print(s.minimum())
s.push(3)
print(s)
print(s.minimum())
s.push(1)
print(s)
print(s.minimum())
s.push(2)
print(s)
print(s.minimum())
s.push(0)
print(s)
print(s.minimum())
s.pop()
print(s)
print(s.minimum())
s.pop()
print(s)
print(s.minimum())
s.pop()
print(s)
print(s.minimum())
s.pop()
print(s)
print(s.minimum())
s.pop()
print(s)
print(s.minimum())
