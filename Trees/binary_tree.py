from collections import deque


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, root):
        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            print(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)


class Tree:

    def __init__(self):
        self.root = None

    q = deque()

    def create_tree(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            temp = self.q[0]
            if temp.left is None:
                temp.left = node
            elif temp.right is None:
                temp.right = node
                self.q.popleft()
        self.q.append(node)
        return self.root

    def print_tree(self):
        if self.root:
            self.root.print_tree(self.root)


tree = Tree()
tree.create_tree(3)
tree.create_tree(9)
tree.create_tree(1)
tree.create_tree(5)
tree.create_tree(10)
tree.create_tree(34)
tree.print_tree()
