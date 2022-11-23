c_ Queue(
    ___ -
        items _    # list

    ___ enqueue item
        ?.a..(item)

    ___ dequeue
        __ l..(items
            r_ ?.p.. 0)

    ___ peek
        __ l..(items
            r_ items[0].value


c_ Node(
    ___ -  value
        ? _ ?
        left _ N..
        right _ N..


c_ BinaryTree(
    ___ -  value
        root _ ? ?

    ___ levelorder start
        __ start __ N..
            r_

        queue _ Queue()
        queue.enqueue(start)
        traversal _    # list

        _____ l..(queue.items) > 0:
            traversal.a..(queue.peek())
            node _ queue.dequeue()

            __ ?.left:
                queue.enqueue(?.left)
            __ ?.right:
                queue.enqueue(?.right)

        r_ traversal


tree _ BinaryTree(3)

tree.root.left _ Node(4)
tree.root.left.left _ Node(6)
tree.root.left.right _ Node(7)

tree.root.left.left.right _ Node(20)

tree.root.right _ Node(5)
tree.root.right.left _ Node(8)
tree.root.right.right _ Node(9)

tree.root.right.left.left _ Node(10)

print(tree.levelorder(tree.root))