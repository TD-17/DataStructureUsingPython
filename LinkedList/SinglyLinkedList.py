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

    def insert_node(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        else:
            self.head = new_node

    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


n = input("Enter number of nodes")
n = int(n)

ll = LinkedList()

while n:
    d = input()
    ll.insert_node(d)
    n = n - 1

ll.print_ll()
