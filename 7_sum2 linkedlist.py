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

    def sum(self, list2):
        p = self.head
        q = list2.head

        result = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                if p.next != None and q.next != None:
                    remaninder = s%10
                    result.append(remaninder)
                else:
                    remaninder = s%10
                    result.append(remaninder)
                    result.append(carry)
            else:
                carry = 0
                result.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return result

list = LinkedList()

list.append(3)
list.append(6)
list.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(8)

print(list.sum(list2))
