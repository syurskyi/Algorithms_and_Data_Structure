c_ Node():
    ___  -  value):
        value = value
        left = N..
        right = N..


c_ BinaryTree():
    ___  -  value):
        root = Node(value)

    ___ preorder  start, traversal):
        # Root -> Left -> Right
        __ start __ N..:
            r_

        traversal.a.. start.value)
        preorder(start.left, traversal)
        preorder(start.right, traversal)

        r_ traversal

    ___ inorder  start, traversal):
        # Left -> Root -> Right
        __ start __ N..:
            r_

        inorder(start.left, traversal)
        traversal.a.. start.value)
        inorder(start.right, traversal)

        r_ traversal

    ___ postorder  start, traversal):
        # Left -> Right -> Root
        __ start __ N..:
            r_

        postorder(start.left, traversal)
        postorder(start.right, traversal)
        traversal.a.. start.value)

        r_ traversal


tree = BinaryTree(3)

tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.preorder(tree.root, []))
print(tree.inorder(tree.root, []))
print(tree.postorder(tree.root, []))