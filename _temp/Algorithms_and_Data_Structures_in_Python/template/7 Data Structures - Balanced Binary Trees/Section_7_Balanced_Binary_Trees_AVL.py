c_ Node o..

    ___ -  data
        data _ data
        height _ 0
        leftChild _ N..
        rightChild _ N..


c_ AVL o..

    ___ -  
        root _ N..

    ___ remove data
        __ root:
            root _ removeNode(data, root)

    ___ insert data
        root _ insertNode(data, root)

    ___ insertNode data, node

        __ n.. node:
            r_ Node(data)

        __ data < node.data:
            node.leftChild _ insertNode(data, node.leftChild)
        ____
            node.rightChild _ insertNode(data, node.rightChild)

        node.height _ max(calcHeight(node.leftChild), calcHeight(node.rightChild)) + 1

        r_ settleViolation(data, node)

    ___ removeNode data, node

        __ n.. node:
            r_ node

        __ data < node.data:
            node.leftChild _ removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild _ removeNode(data, node.rightChild)
        ____

            __ n.. node.leftChild and n.. node.rightChild:
                print("Removing a leaf node...")
                del node
                r_ N..

            __ n.. node.leftChild:
                print("Removing a node with a right child...")
                tempNode _ node.rightChild
                del node
                r_ tempNode
            elif n.. node.rightChild:
                print("Removing a node with a left child...")
                tempNode _ node.leftChild
                del node
                r_ tempNode

            print("Removing node with two children...")
            tempNode _ getPredecessor(node.leftChild);
            node.data _ tempNode.data;
            node.leftChild _ removeNode(tempNode.data, node.leftChild);

        __ n.. node:
            r_ node;  # if the tree had just a single node

        node.height _ max(calcHeight(node.leftChild), calcHeight(node.rightChild)) + 1;

        balance _ calcBalance(node);

        # doubly left heavy situation
        __ balance > 1 and calcBalance(node.leftChild) >_ 0:
            r_ rotateRight(node);

        # left right case
        __ balance > 1 and calcBalance(node.leftChild) < 0:
            node.leftChild _ rotateLeft(node.leftChild);
            r_ rotateRight(node);

        # right right case
        __ balance < -1 and calcBalance(node.rightChild) <_ 0:
            r_ rotateLeft(node);

        # right left case
        __ balance < -1 and calcBalance(node.rightChild) > 0:
            node.rightChild _ rotateRight(node.rightChild);
            r_ rotateLeft(node);

        r_ node;

    ___ getPredecessor node

        __ node.rightChild:
            r_ getPredecessor(node.rightChild);

        r_ node;

    ___ settleViolation data, node

        balance _ calcBalance(node);

        # this is the Case I !!!! left-left heavy situation
        __ balance > 1 and data < node.leftChild.data:
            print("Left left heavy tree...")
            r_ rotateRight(node);

        # this is the Case II right-right !!!!
        __ balance < -1 and data > node.rightChild.data:
            print("Right right heavy tree...")
            r_ rotateLeft(node);

        # left-right situation
        __ balance > 1 and data > node.leftChild.data:
            print("Tree is leaft right heavy...");
            node.leftChild _ rotateLeft(node.leftChild);
            r_ rightRotation(node);

        # right-left situation
        __ balance < -1 and data < node.rightChild.data:
            node.rightChild _ rotateRight(node.rightChild);
            r_ rotateLeft(node);

        r_ node;

    ___ settleViolation data, node

        balance _ calcBalance(node);

        # case 1  -> left left heavy situation
        __ balance > 1 and data < node.leftChild.data:
            print("Left left heavy situation...");
            r_ rotateRight(node);

        # case 2 --> right right heavy situation --> single left rotation
        __ balance < - 1 and data > node.rightChild.data:
            print("Right right heavy situation...");
            r_ rotateLeft(node);

        __ balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation...");
            node.leftChild _ rotateLeft(node.leftChild);
            r_ rotateRight(node);

        __ balance < - 1 and data < node.rightChild.data:
            print("Right left heavy situation...");
            node.rightChild _ rotateRight(node.rightChild);
            r_ rotateLeft(node);

        r_ node;

    ___ calcHeight node

        __ n.. node:
            r_ -1;

        r_ node.height;

    # if it returns value > 1  it means it is a left heavy tree --> right rotation
    #  ......             < -1   right heavy tree -> left rotation
    ___ calcBalance node

        __ n.. node:
            r_ 0;

        r_ calcHeight(node.leftChild) - calcHeight(node.rightChild);

    ___ traverse 
        __ root:
            traverseInorder(root);

    ___ traverseInorder node

        __ node.leftChild:
            traverseInorder(node.leftChild);

        print("%s " % node.data);

        __ node.rightChild:
            traverseInorder(node.rightChild);

    ___ rotateRight node

        print("Rotating to the right on node ", node.data);

        tempLeftChild _ node.leftChild;
        t _ tempLeftChild.rightChild;

        tempLeftChild.rightChild _ node;
        node.leftChild _ t;

        node.height _ max(calcHeight(node.leftChild), calcHeight(node.rightChild)) + 1;
        tempLeftChild.height _ max(calcHeight(tempLeftChild.leftChild),
                                   calcHeight(tempLeftChild.rightChild)) + 1;

        r_ tempLeftChild;

    ___ rotateLeft node

        print("Rotating to the left on node ", node.data);

        tempRightChild _ node.rightChild;
        t _ tempRightChild.leftChild;

        tempRightChild.leftChild _ node;
        node.rightChild _ t;

        node.height _ max(calcHeight(node.leftChild), calcHeight(node.rightChild)) + 1;
        tempRightChild.height _ max(calcHeight(tempRightChild.leftChild),
                                    calcHeight(tempRightChild.rightChild)) + 1;

        r_ tempRightChild;


avl _ AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)
avl.remove(15)
avl.remove(20)
avl.traverse()
