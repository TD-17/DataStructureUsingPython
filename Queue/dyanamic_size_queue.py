class QueueNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = QueueNode(data)
        if self.front is None:
            self.front = newNode
            self.rear = self.front
            return
        self.rear.next = newNode
        self.rear = newNode

    def is_empty(self):
        return self.front == None

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next
        data = temp.data
        temp = None
        return data

    def print(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next


q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.print()
print(q.dequeue())
q.dequeue()
q.dequeue()
q.dequeue()
print("End of dequeue")
q.print()
