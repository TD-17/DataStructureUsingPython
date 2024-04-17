class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        temp = self.head
        if self.head is not None:
            while temp.next is not self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def print(self):
        temp = self.head.next
        if self.head is None:
            print("Nothing to print")
            return

        print("This is the list")

        print(self.head.data)

        while temp is not self.head:
            print(temp.data)
            temp = temp.next

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is self.head or self.head.data is data:
            self.head = None
            return

        temp = self.head
        while temp.next is not self.head and temp.next.data is not data:
            temp = temp.next
        if temp.next.data is data:
            d = temp.next
            temp.next = d.next
            d = None
        else:
            print("Given data not found")


cll = CircularLinkedList()
cll.push(3)
cll.push(8)
cll.push(9)
cll.push(1)
cll.push(2)
cll.push(7)
cll.push(4)
cll.print()
cll.delete(6)
