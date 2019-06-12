class Node:

    def __init__(self, data):
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

#We use 2 pointers, p and q then changing the pointers to change direction of the linked list

        def rotate(self, index):
            p = self.head
            q = self.head
            count = 0
            prev = None

            while p and count < index:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev

            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None



list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(1)
list.append(1)
list.append(12)

print(list)
list.rotate(3)
print(list)
