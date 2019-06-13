class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        cur = self.head
        if self.head != None:
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

    def display(self):
        show = []
        cur = self.head
        while cur != None:
            show.append(cur.data)
            cur = cur.next
        return show

    def __str__(self):
        show = self.display()
        return(str(show))

    def isPalindrome(self):
        s = ""
        cur = self.head
        while cur:
            s += str(cur.data)
            cur = cur.next
        return s == s[::-1]

    def isPalindrome2(self):
        ## using a stack approach.. pop element to see if they match p.data traversing from the front
        stack = []
        p = self.head
        while p:
            stack.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = stack.pop()
            if p.data != data:
                return False
            p = p.next
        return True




list = LinkedList()
list.append("R")
list.append("R")
list.append("A")
list.append("D")
list.append("A")
list.append("R")
list.append("R")

print(list.isPalindrome2())
