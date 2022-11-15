class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        pass

    def _in_order(self, curr):
        pass

    def pre_order(self):
        '''root, left, right'''
        pass

    def _pre_order(self, curr):
        pass

    def post_order(self):
        '''left, right, root'''
        pass

    def _post_order(self, curr):
        pass

    def find_val(self, key):
        pass

    def _find_val(self, curr, key):
        pass

    def delete_val(self, key):
        pass

    def _delete_val(self, curr, prev, is_left, key):
        pass

tree = BSTDemo()
tree.insert("F")
print(tree.root.data)
tree.insert("C")
print(tree.root.left_child.data)
tree.insert("G")
print(tree.root.right_child.data)
tree.insert("A")
print(tree.root.left_child.left_child.data)
tree.insert("B")
print(tree.root.left_child.left_child.right_child.data)
tree.insert("K")
print(tree.root.right_child.right_child.data)
tree.insert("H")
print(tree.root.right_child.right_child.left_child.data)
