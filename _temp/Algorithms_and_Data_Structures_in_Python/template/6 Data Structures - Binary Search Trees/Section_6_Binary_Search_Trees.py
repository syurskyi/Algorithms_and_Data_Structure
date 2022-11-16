c_ Node o..

    ___ -  data
        data _ data
        leftChild _ N..
        rightChild _ N..


c_ BinarySearchTree o..

    ___ -  
        root _ N..

    ___ insert data
        __ n.. root:
            root _ Node(data)
        ____
            insertNode(data, root)

    # O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> it can reduced to O(N) --> AVL RBT are needed !!!!!
    ___ insertNode data, node

        __ data < node.data:
            __ node.leftChild:
                insertNode(data, node.leftChild)
            ____
                node.leftChild _ Node(data)
        ____
            __ node.rightChild:
                insertNode(data, node.rightChild)
            ____
                node.rightChild _ Node(data)

    # O(logN)
    ___ removeNode data, node

        __ n.. node:
            r_ node

        __ data < node.data:
            node.leftChild _ removeNode(data, node.leftChild)
        ____ data > node.data:
            node.rightChild _ removeNode(data, node.rightChild)
        ____

            __ n.. node.leftChild ___ n.. node.rightChild:
                print("Removing a leaf node...")
                d.. node
                r_ N..

            __ n.. node.leftChild:  # node !!!
                print("Removing a node with single right child...")
                tempNode _ node.rightChild
                d.. node
                r_ tempNode
            ____ n.. node.rightChild:  # node instead of self
                print("Removing a node with single left child...")
                tempNode _ node.leftChild
                d.. node
                r_ tempNode

            print("Removing node with two children....")
            tempNode _ getPredecessor(node.leftChild)  # self instead of elf  + get predecessor
            node.data _ tempNode.data
            node.leftChild _ removeNode(tempNode.data, node.leftChild)

        r_ node  # !!!!!!!!!!!!

    ___ getPredecessor node

        __ node.rightChild:
            r_ getPredecessor(node.rightChild)

        r_ node

    ___ remove data
        __ root:
            root _ removeNode(data, root)

    # O(logN)
    ___ getMinValue 
        __ root:
            r_ getMin(root)

    ___ getMin node

        __ node.leftChild:
            r_ getMin(node.leftChild)

        r_ node.data

    # O(logN)
    ___ getMaxValue 
        __ root:
            r_ getMax(root)

    ___ getMax node

        __ node.rightChild:
            r_ getMax(node.rightChild)

        r_ node.data

    ___ traverse 
        __ root:
            traverseInOrder(root)

        # O(N)

    ___ traverseInOrder node

        __ node.leftChild:
            traverseInOrder(node.leftChild)

        print("%s " % node.data)

        __ node.rightChild:
            traverseInOrder(node.rightChild)


bst _ BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)
bst.remove(10)

bst.traverse()
