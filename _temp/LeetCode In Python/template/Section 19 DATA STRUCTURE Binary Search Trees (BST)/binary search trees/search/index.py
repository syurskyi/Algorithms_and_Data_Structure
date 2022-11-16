

c_ Node:
    ___ -  value
        left _ N..
        right _ N..
        data _ value


___ i.. (root, node
    __(root __ N..
        root _ node
        r_

    __(root.data < node.data
        __(root.right __ N..
            root.right _ node
        ____
            i.. (root.right, node)
    ____
        __(root.left __ N..
            root.left _ node
        ____
            i.. (root.left, node)


___ search(node, key
    print("Current Node is: ", node.data)
    __(node __ N..
        print("No node found")
        r_ N..
    __(node.data __ key
        print("Node found !")
        r_ node

    __(node.data < key
        r_ search(node.right, key)

    r_ search(node.left, key)


#	           5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree _ Node(5)

i.. (tree, Node(3))


i.. (tree, Node(2))

i.. (tree, Node(4))

i.. (tree, Node(7))

i.. (tree, Node(6))

i.. (tree, Node(8))

search(tree, 8)
