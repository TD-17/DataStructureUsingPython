class MaxPriorityQueue:
    # This class implements priority queue using max heap
    def __init__(self):
        self.heap = [0] * 40
        self.size = 0

    def parent(self, i):
        temp = (i - 1) // 2
        return temp

    def left_child(self, i):
        return (i * 2) + 1

    def right_child(self, i):
        return (i * 2) + 2

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def shift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def shift_down(self, i):
        max_index = i
        l = self.left_child(i)
        if l < self.size and self.heap[l] > self.heap[max_index]:
            max_index = l
        r = self.right_child(i)
        if r < self.size and self.heap[r] > self.heap[max_index]:
            max_index = r
        if i is not max_index:
            self.swap(i, max_index)
            self.shift_down(max_index)

    def insert(self, value):
        i = self.size
        print("size is", i)
        self.heap[i] = value
        self.shift_up(i)
        self.size = self.size + 1

    def extract_max(self):
        if self.size is 0:
            print("heap is empty")
            return
        value = self.heap[0]
        print("The max value is", value)
        self.heap[0] = self.heap[self.size - 1]
        self.size = self.size - 1
        self.shift_down(0)

    def print(self):
        i = 0
        while i < self.size:
            print(self.heap[i])
            i = i + 1


pq = MaxPriorityQueue()
pq.insert(45)
pq.insert(20)
pq.insert(14)
pq.insert(12)
pq.insert(31)
pq.insert(7)
pq.insert(11)
pq.insert(13)
pq.insert(7)
pq.print()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
pq.extract_max()
