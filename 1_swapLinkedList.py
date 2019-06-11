class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, head = None):
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode

    def display(self):
        enum = []
        cur = self.head
        while cur.next:
            cur = cur.next
            enum.append(cur.data)
        return enum

    def __str__(self):
        show = self.display()
        return(str(show))

    def swap(self, key1, key2):
        """A -> B -> C -> D swap B and C  or A and B
           A -> C -> B -> D
        """
        if key1 == key2:
            return

        cur_1  = self.head
        prev_1 = None

        while cur_1 and cur_1.data != key1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        cur_2  = self.head
        prev_2 = None

        while cur_2 and cur_2.data != key2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

list = LinkedList()
list.append("A")
list.append("B")
list.append("C")
list.append("D")

print(list)

list.swap("D", "B")
print(list)
