

c_ Node:
    ___ -  value
        left _ N..
        right _ N..
        data _ value


___ insert(root, node
    __(root __ N..
        root _ node
        r_

    __(root.data < node.data
        __(root.right __ N..
            root.right _ node
        ____
            insert(root.right, node)
    ____
        __(root.left __ N..
            root.left _ node
        ____
            insert(root.left, node)


___ search(node, key
    print("Current Node is: ", node.data)
    __(node __ N..
        print("No node found")
        r_ N..
    __(node.data == key
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

insert(tree, Node(3))


insert(tree, Node(2))

insert(tree, Node(4))

insert(tree, Node(7))

insert(tree, Node(6))

insert(tree, Node(8))

search(tree, 8)
