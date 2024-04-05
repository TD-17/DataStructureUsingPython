# To implement a linked list in python, we will use classes.
# A class is user defined prototype from which objects are created.
# Class bundles data and functionality together.
# Each class instance can have attributes attached to it for maintaining its state.
# Class instances can also have methods (defined by their class) for modifying their state.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.last_node = None

    def push(self, new_data):
        if self.last_node is None:
            self.head = Node(new_data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(new_data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


obj = LinkedList()
n = 5
for i in range(n):
    data = int(input('Enter data item: '))
    obj.push(data)
obj.display()
