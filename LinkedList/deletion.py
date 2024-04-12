class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data), end=" "),
            temp = temp.next
        print()

    def delete(self, index):
        temp = self.head
        if index == 1:
            self.head = temp.next
            temp = None
            return
        while (index and temp is not None):
            prev = temp
            temp = temp.next
            index = index - 1
        if temp is not None:
            prev.next = temp.next
        temp = None

    def delete_tail(self):
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        temp = None

    def insert(self, index, data):
        new_node = Node(data)
        if index == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        index = index - 1
        while (index and temp is not None):
            prev = temp
            temp = temp.next
            index = index - 1
        if index is not 0:
            return
        prev.next = new_node
        new_node.next = temp


# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(3)
llist.push(2)

llist.printList()
llist.delete(2)
llist.printList()
llist.delete_tail()
llist.printList()
llist.insert(39, 5)
llist.printList()
