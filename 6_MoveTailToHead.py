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

    def MoveTailToHead(self):
        LastNode = self.head

        while LastNode.next:
            prev = LastNode
            LastNode  = LastNode.next
        LastNode.next = self.head
        prev.next = None
        self.head = LastNode

list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
print(list)
list.MoveTailToHead()
print(list)
