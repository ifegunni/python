class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        cur = self.head

        while cur.next:
            cur = cur.next
        cur.next = newNode

    def display(self):
        show = []
        cur = self.head

        while cur.next:
            cur = cur.next
            show.append(cur.data)
        return show

    def __str__(self):
        show = self.display()
        return(str(show))

    def length(self, Node):
        if Node.next is None:
            return 0
        else:
            return 1 + self.length(Node.next)

    def nthToLast(self, index):
        cur = self.head
        n = int(self.length(cur))

        while cur.next:
            cur = cur.next
            if n  == index:
                return cur.data
            n -= 1
        if cur is None:
            return






list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(1)
list.append(4)
list.append(12)

print(list.nthToLast(2))
