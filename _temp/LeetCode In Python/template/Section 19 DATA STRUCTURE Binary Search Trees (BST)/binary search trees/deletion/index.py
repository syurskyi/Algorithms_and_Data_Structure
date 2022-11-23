

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


___ minValueNode(node
    _____(?.left __ n.. N..
        node _ ?.left
    r_ node


___ deleteNode(node, key
    __(node __ N..
        r_ node
    # If the key to be deleted is smaller than the node's
    # key then it lies in  left subtree
    __ key < ?.d..
        ?.left _ deleteNode(?.left, key)
    # If the kye to be delete is greater than the node's key
    # then it lies in right subtree
    ____(key > ?.data
        ?.right _ deleteNode(?.right, key)
    # If key is same as node's key, then this is the node
    # to be deleted
    ____
        # Node with only one child or no child
        __ ?.left __ N..
            temp _ ?.right
            node _ N..
            r_ temp
        ____ ?.right __ N..
            temp _ ?.left
            node _ N..
            r_ temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp _ minValueNode(?.right)
        # Copy the inorder successor's content to this node
        ?.data _ ?.data
        # Delete the inorder successor
        ?.right _ deleteNode(?.right, ?.data)

    r_ node


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

deleteNode(tree, 7)

#	           5
#       /  	      \
#     3	            8
#   /   \        /     \
#  2     4      6       None


# 5 3 2 4 8 6
preorder(tree)
