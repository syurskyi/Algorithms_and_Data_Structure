c_ Node(
    ___ -  value
        ? _ ?
        left _ N..
        right _ N..


c_ BinaryTree(
    ___ -  value
        root _ ? ?

    ___ preorder start, traversal
        # Root -> Left -> Right
        __ start __ N..
            r_

        traversal.a..(start.value)
        preorder(start.left, traversal)
        preorder(start.right, traversal)

        r_ traversal

    ___ inorder start, traversal
        # Left -> Root -> Right
        __ start __ N..
            r_

        inorder(start.left, traversal)
        traversal.a..(start.value)
        inorder(start.right, traversal)

        r_ traversal

    ___ postorder start, traversal
        # Left -> Right -> Root
        __ start __ N..
            r_

        postorder(start.left, traversal)
        postorder(start.right, traversal)
        traversal.a..(start.value)

        r_ traversal


tree _ BinaryTree(3)

tree.root.left _ Node(4)
tree.root.left.left _ Node(6)
tree.root.left.right _ Node(7)

tree.root.right _ Node(5)
tree.root.right.left _ Node(8)
tree.root.right.right _ Node(9)

print(tree.preorder(tree.root,    # list))
print(tree.inorder(tree.root,    # list))
print(tree.postorder(tree.root,    # list))