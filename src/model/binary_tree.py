import random


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left: BinaryNode = None
        self.right: BinaryNode = None

    def __repr__(self):
        return f'{self.value}'
    

class BinarySearchTree:
    def __init__(self):
        self.root: BinaryNode = None

    def insert(self, value, current_node = None):
        new_node = BinaryNode(value)
        if current_node is None:
            current_node = self.root
        if self.root is None:
            self.root = new_node
            return
        if self.root.value == value:
            return 'Nodo repetido'
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
                return
            else:
                self.insert(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
                return
            else:
                self.insert(value, current_node.right)

    def search(self, value, current_node = None):
        if current_node is None:
            current_node = self.root
        if self.root is None:
            return 'No hay nodos'
        if value == current_node.value:
            return True
        if value < current_node.value:
            if current_node.left is not None:
                if (self.search(value, current_node.left)) is True:
                    return True
        else:
            if current_node.right is not None:
                if (self.search(value, current_node.right)) is True:
                    return True
        return False

    def print(self, node, prefix="", is_left=True):
            if not node:
              print("Empty Tree")
              return
            if node.right:
              self.print(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
            if node.left:
              self.print(node.left, prefix + ("    " if is_left else "│   "), True)

bst = BinarySearchTree()

for i in range(40):
    bst.insert(random.randint(1, 100))

bst.insert(10)
bst.print(bst.root)
print(bst.search(10))