def merge(self, list):
        p = self.head
        q = list2.head
        s = None

        if not p: # check if the list p is empty
            return q
        if not q: # check if the list q is empty
            return p

        if p and q:
            if p.data <= q.data: 
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            newHead = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next

            else:
                s.next = q
                s = q
                q = s.next

        if not p:  # if we get to the end of p before q then set the pointer to q
            s.next = q

        if not q:
            s.next = p

        return newHead







list = LinkedList()
list2 = LinkedList()


list.append("1")
list.append("5")
list.append("7")
list.append("9")
list.append("10")

# print(list)


list2.append("2")
list2.append("3")
list2.append("4")
list2.append("6")
list2.append("8")

# print(list2)


list.merge(list2)
print(list)
