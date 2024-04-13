class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = new_node
        self.head.prev = temp
        temp.next = self.head
        self.head = temp

    def print_linkedlist(self):
        if self.head is None:
            print("Nothing to print, linked list is empty")
            return
        current = self.head
        print("Printing list")
        while current is not None:
            print(current.data)
            current = current.next

    def del_from_start(self):
        if self.head is None:
            print("Nothing to delete, list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        print("Printing deleted data", temp.data)
        temp.next = None
        temp = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print("Previous node is", new_node.prev.data)


ll = DoublyLinkedList()
ll.insert_at_begin(3)
ll.insert_at_begin(4)
ll.insert_at_begin(6)
ll.insert_at_begin(7)
ll.insert_at_begin(2)
ll.insert_at_begin(8)
ll.insert_at_begin(9)
ll.print_linkedlist()
ll.del_from_start()
ll.print_linkedlist()
ll.del_from_start()
ll.print_linkedlist()
ll.insert_at_end(6)
ll.print_linkedlist()
ll.insert_at_end(2)
ll.print_linkedlist()
