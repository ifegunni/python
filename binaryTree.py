class Stack(object):
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def peek(self):
        if not self.isEmpty():
            return self.item[-1]

    def size(self):
        return len(self.item)

    def __len__(self):
        return self.size()


class Queue(object):
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.item.pop()

    def isEmpty(self):
        return len(self.item) == 0

    def peek(self):
        if not self.isEmpty():
            return self.item[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_Tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type == "Reverselevelorder":
            return self.reverseOrder_print(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node  = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.en
                queue(node.right)
        return traversal

    def reverseOrder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)

            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    def height(self, start):
        if start is None:
            return -1

        left_height = self.height(start.left)
        right_height = self.height(start.right)
        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)

            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def sizeRecur(self, node):
        if node is None:
            return 0

        left = self.sizeRecur(node.left)
        right = self.sizeRecur(node.right)
        size = 1+left + right
        return size


    def preorder_print(self, start, traversal):
        """Roots --> Left --> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -->Roots  --> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -->Right  --> Roots """
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


"""
node = i
node.left = 2i +1
node.right = 2i+2

(i) Adjacency list
(ii) Adjacency Matrix

Adjacency list:
adjlist = {1: [2,3],2: [4,5 ],3: [6,7] }

adjlist = {}

def appendEdge(id1,id2,adjlist):
    #adjlist[id1] = [id2] + adjlist.get(id1,[])
    # check if the id is in the dictionary
    if id1 in adjlist:
        adjlist[id1].append(id2)
    else:
        adjlist[id1] = [id2]


"""

print(tree.print_Tree("Reverselevelorder"))

print(tree.height(tree.root))
print(tree.sizeRecur(tree.root))


# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
#
# print(queue)
