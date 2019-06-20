class Stack:

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def get_Stack(self):
        return self.item

    def peek(self):
        if not self.is_empty():
            return self.item[-1]

