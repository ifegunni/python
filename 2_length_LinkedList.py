def length_iter(self):
        cur = self.head
        count = 0
        while cur.next:
            cur = cur.next
            count += 1
        return count

    def length_recursive(self, Node):
        if Node.next is None:
            return 0
        else:
            return 1 + self.length_recursive(Node.next)
