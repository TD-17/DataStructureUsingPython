class QueueNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = QueueNode(data)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.rear is None:
            print("Queue is empty")

        if self.rear is self.front:
            self.rear = None
            self.front = None
            return
        temp = self.front
        self.front = self.front.next
        temp = None

    def display(self):
        if self.rear is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp is not self.rear:
            print(temp.data)
            temp = temp.next
        print(temp.data)


cq = CircularQueue()
cq.enqueue(7)
cq.enqueue(8)
cq.enqueue(5)
cq.enqueue(6)
cq.enqueue(1)
cq.enqueue(9)
cq.display()
print("dequeue")
cq.dequeue()
cq.display()
print("dequeue")
cq.dequeue()
cq.display()
