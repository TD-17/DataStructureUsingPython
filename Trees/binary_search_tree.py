class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_data(self, data):
        node = Node(data)
        if data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_data(data)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_data(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


tree = Node(12)
tree.insert_data(3)
tree.insert_data(4)
tree.insert_data(6)
tree.insert_data(7)
tree.print_tree()
