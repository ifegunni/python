class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_data = Node(data)
        current = self.head
        if self.head != None:
            while current.next:
                current = current.next
            current.next = new_data
        else:
            self.head = new_data


    def display(self):
        arr = []

        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    def __str__(self):
        show = self.display()
        return str(show)

    def reverse_Using_Stack(self):
        stack = Stack()

        current = self.head
        while current:
            stack.push(current)
            current = current.next

        current = stack.top()
        self.head = current
        stack.pop()

        while not stack.isEmpty():
            current.next = stack.top()
            stack.pop()
            current = current.next
        current.next = None




class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def top(self):
        if not self.isEmpty():
            return self.item[-1]

    def __str__(self):
        return str(self.item)



list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)

print(list)
list.reverse_Using_Stack()

print(list)
