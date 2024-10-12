#https://www.geeksforgeeks.org/stack-in-python/
class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.root = None

    def push(self, data):
        stack_node = StackNode(data)
        stack_node.next = self.root
        self.root = stack_node

    def top(self):
        if self.root is None:
            print("Stack is empty")
            return

        print(self.root.data)

    def pop(self):
        if self.root is None:
            print("Stack is empty")
            return

        temp = self.root
        self.root = temp.next
        temp = None


stack = Stack()
stack.push(5)
stack.push(8)
stack.push(9)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(7)
stack.push(4)
stack.top()
stack.pop()
stack.top()
stack.pop()
stack.top()
stack.pop()
stack.top()
stack.pop()
stack.top()
