c_ Node():
    ___  -  value):
        value = value
        left = N..
        right = N..


c_ BinaryTree():
    ___  -  value):
        root = Node(value)


tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)