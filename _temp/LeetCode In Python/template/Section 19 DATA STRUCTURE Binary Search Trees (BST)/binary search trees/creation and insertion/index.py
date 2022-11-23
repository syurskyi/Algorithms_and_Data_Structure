

c_ Node
    ___ -  value
        left _ N..
        right _ N..
        data _ value


___ i.. (root, node
    __(root __ N..
        root _ node
        r_

    __(root.data < ?.data
        __(root.right __ N..
            root.right _ node
        ____
            i.. (root.right, node)
    ____
        __(root.left __ N..
            root.left _ node
        ____
            i.. (root.left, node)


___ preorder(node
    __(node __ n.. N..
        print(?.data)
        preorder(?.left)
        preorder(?.right)


#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree _ Node(5)

#	         5
#       /  	      \
#     None	       None

i.. (tree, Node(3))

#	         5
#       /  	      \
#     3	            None

i.. (tree, Node(2))

#	         5
#       /  	      \
#     3	            None
#   /
#  2
i.. (tree, Node(4))

#	         5
#       /  	      \
#     3	            None
#   /   \
#  2     4
i.. (tree, Node(7))

#	         5
#       /  	      \
#     3	            7
#   /   \
#  2     4
i.. (tree, Node(6))

#	         5
#       /  	      \
#     3	            7
#   /   \        /
#  2     4      6
i.. (tree, Node(8))

#	         5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8


# 5 3 2 4 7 6 8
preorder(tree)
