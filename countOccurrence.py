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



## iterative approach 
    def countOcc(self, key):
        cur = self.head
        value = 0

        while cur:
            if cur.data == key:
                value += 1
            cur = cur.next
        return value

## Recursive approach
    def countOccRecur(self, node, key):

        if not node:
            return 0
        if node.data == key:
            return 1 + self.countOccRecur(node.next, key)
        else:
            return self.countOccRecur(node.next, key)



list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(1)
list.append(1)
list.append(12)

print(list.countOcc(1))
