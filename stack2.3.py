class Stack:

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def empty(self):
        return self.item == []

    def peek(self):
        if not self.empty():
            return self.item[-1]

def divideBy2(number):
    string = ""
    s = Stack()
    while number > 0:
        remainder = number%2
        s.push(remainder)
        number = number// 2

    while not s.empty():
        string += str(s.pop())

    return string

print(divideBy2(242))
