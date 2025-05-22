class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return f'{self.value}'
    

class GeneralTree:
    def __init__(self):
        self.root: Node = None
        self.added_values = []
    
    def insert(self, parent, child, current_node = None):
        if current_node is None:
            current_node = self.root
        if self.root is None:
            self.root = Node(parent)
            self.root.children.append(Node(child))
            self.added_values.append(parent)
            self.added_values.append(child)
        else:
            if current_node.value == parent:
                if child not in self.added_values:
                    current_node.children.append(Node(child))
                    self.added_values.append(child)
                    return True
            else:
                for ch in current_node.children:
                    if (self.insert(parent, child, ch)) is True:
                        return True
                    
    def BFS(self, value):
        start = self.root
        if start is None:
            return []
        parent_map = {start: None}
        queue = [start]
        while queue:
            current = queue.pop(0)
            if current.value == value:
                path = []
                while current is not None:
                    path.insert(0, current)
                    current = parent_map[current]
                return path
            for child in current.children:
                if child not in parent_map:
                    parent_map[child] = current
                    queue.append(child)
        return []
    
    def delete_tree(self):
        self.root = None
        self.added_values = []
                    
    def print(self, node=None, prefix="", is_last=True):
        if node is None:
            node = self.root
        if node is None:
            print("Arbol vacio")
            return
        connector = "└── " if is_last else "├── "
        print(prefix + connector + str(node))
        new_prefix = prefix + ("    " if is_last else "│   ")
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            is_last_child = (i == child_count - 1)
            self.print(child, new_prefix, is_last_child)


    
# gt = GeneralTree()
# gt.insert(4,1)
# gt.insert(4,2)
# gt.insert(4,3)
# gt.insert(4,5)
# gt.insert(1, 10)
# gt.insert(2, 11)
# gt.insert(10, 12)
# gt.insert(5, 10)
# gt.insert(10, 66)
# gt.insert(10, 54)
# gt.insert(2, 54)
# gt.insert(12, 54)
# gt.insert(54, 540)
# gt.insert(540, 541)
# gt.insert(10, 666)
# gt.insert(10, 666)

# print(gt.BFS(666))
# gt.print()

# gt.delte_tree()
# gt.print()

# gt.insert(4,1)
# gt.insert(4,2)
# gt.insert(4,3)
# gt.insert(4,5)
# gt.insert(1, 10)
# gt.insert(2, 11)
# gt.insert(10, 12)
# gt.insert(5, 10)
# gt.insert(10, 66)
# gt.insert(10, 54)
# gt.insert(2, 54)
# gt.insert(12, 54)
# gt.insert(54, 540)
# gt.insert(540, 541)
# gt.insert(10, 666)
# gt.insert(10, 666)
# gt.print()

