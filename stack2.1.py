class Stack:

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def get_Stack(self):
        return self.item

    def peek(self):
        if not self.is_empty():
            return self.item[-1]

def is_Parath_Balance(string):
    y = Stack()
    isBalance = True
    index = 0

    while index < len(string) and isBalance:
        paren = string[index]
        if paren in "({[":
            y.push(paren)
        else:
            if y.is_empty():
                isBalance = False
            else:
                top = y.pop()
                if not is_match(top, paren):
                    isBalance = False
        index += 1

    if y.is_empty() and isBalance:
        return True
    else:
        return False


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True

    elif p1 == "{" and p2 == "}":
        return True

    elif p1 =="[" and p2 =="]":
        return True

    else:
        return False


print(is_Parath_Balance("{[(]}"))



# s = Stack()
# print(s.is_empty())
# s.push("{")
# s.push("(")
# s.push(")")
# s.push("}")
# print(s.get_Stack())
# print(s.is_empty())
# print(s.peek())
# s.pop()
# print(s.get_Stack())
# print(s.peek())
