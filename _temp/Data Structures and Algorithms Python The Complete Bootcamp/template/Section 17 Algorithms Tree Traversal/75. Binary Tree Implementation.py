c_ Node(
    ___ -  value
        value _ value
        left _ N..
        right _ N..


c_ BinaryTree(
    ___ -  value
        root _ ? ?


tree _ BinaryTree(3)

tree.root.left _ Node(4)
tree.root.left.left _ Node(6)
tree.root.left.right _ Node(7)

tree.root.right _ Node(5)
tree.root.right.left _ Node(8)
tree.root.right.right _ Node(9)