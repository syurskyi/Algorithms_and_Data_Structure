c_ Node o..

    ___ -  data
        ? _ ?
        height _ 0
        leftChild _ N..
        rightChild _ N..


c_ AVL o..

    ___ -  
        root _ N..

    ___ remove data
        __ root
            r.. _ ? ? ?

    ___ i..  data
        r.. _ ? ?  ?

    ___ insertNode data node

        __ n.. ?
            r_ ? ?

        __ d.. < ?.d..
            ?.l.. _ ? ?  ?.l..
        ____
            ?.r.. _ ? ?  ?.r..

        ?.h.. _ m__(calcHeight(?.l.., calcHeight(?.r..)) + 1

        r_ settleViolation(data, node)

    ___ removeNode data, node

        __ n.. node:
            r_ node

        __ data < ?.d..
            ?.l.. _ ? ? ?.l..
        ____ data > ?.d..
            ?.r.. _ ? ? ?.r..
        ____

            __ n.. ?.l.. ___ n.. ?.r..
                print("Removing a leaf node...")
                d.. node
                r_ N..

            __ n.. ?.l..
                print("Removing a node with a right child...")
                tempNode _ ?.r..
                d.. node
                r_ tempNode
            ____ n.. ?.r..
                print("Removing a node with a left child...")
                tempNode _ ?.l..
                d.. node
                r_ tempNode

            print("Removing node with two children...")
            tempNode _ getPredecessor(?.l..;
            ?.data _ tempNode.data;
            ?.l.. _ removeNode(tempNode.data, ?.l..;

        __ n.. node:
            r_ node;  # if the tree had just a single node

        ?.height _ m__(calcHeight(?.l.., calcHeight(?.r..)) + 1;

        balance _ calcBalance(node);

        # doubly left heavy situation
        __ balance > 1 ___ calcBalance(?.l.. >_ 0:
            r_ rotateRight(node);

        # left right case
        __ balance > 1 ___ calcBalance(?.l.. < 0:
            ?.l.. _ rotateLeft(?.l..;
            r_ rotateRight(node);

        # right right case
        __ balance < -1 ___ calcBalance(?.r.. <_ 0:
            r_ rotateLeft(node);

        # right left case
        __ balance < -1 ___ calcBalance(?.r.. > 0:
            ?.r.. _ rotateRight(?.r..;
            r_ rotateLeft(node);

        r_ node;

    ___ getPredecessor node

        __ ?.r..
            r_ getPredecessor(?.r..;

        r_ node;

    ___ settleViolation data, node

        balance _ calcBalance(node);

        # this is the Case I !!!! left-left heavy situation
        __ balance > 1 ___ data < ?.l...data:
            print("Left left heavy tree...")
            r_ rotateRight(node);

        # this is the Case II right-right !!!!
        __ balance < -1 ___ data > ?.r...data:
            print("Right right heavy tree...")
            r_ rotateLeft(node);

        # left-right situation
        __ balance > 1 ___ data > ?.l...data:
            print("Tree is leaft right heavy...");
            ?.l.. _ rotateLeft(?.l..;
            r_ rightRotation(node);

        # right-left situation
        __ balance < -1 ___ data < ?.r...data:
            ?.r.. _ rotateRight(?.r..;
            r_ rotateLeft(node);

        r_ node;

    ___ settleViolation data, node

        balance _ calcBalance(node);

        # case 1  -> left left heavy situation
        __ balance > 1 ___ data < ?.l...data:
            print("Left left heavy situation...");
            r_ rotateRight(node);

        # case 2 --> right right heavy situation --> single left rotation
        __ balance < - 1 ___ data > ?.r...data:
            print("Right right heavy situation...");
            r_ rotateLeft(node);

        __ balance > 1 ___ data > ?.l...data:
            print("Left right heavy situation...");
            ?.l.. _ rotateLeft(?.l..;
            r_ rotateRight(node);

        __ balance < - 1 ___ data < ?.r...data:
            print("Right left heavy situation...");
            ?.r.. _ rotateRight(?.r..;
            r_ rotateLeft(node);

        r_ node;

    ___ calcHeight node

        __ n.. node:
            r_ -1;

        r_ ?.height;

    # if it returns value > 1  it means it is a left heavy tree --> right rotation
    #  ......             < -1   right heavy tree -> left rotation
    ___ calcBalance node

        __ n.. node:
            r_ 0;

        r_ calcHeight(?.l.. - calcHeight(?.r..;

    ___ traverse 
        __ root:
            traverseInorder(root);

    ___ traverseInorder node

        __ ?.l..
            traverseInorder(?.l..;

        print("%s " _ ?.data);

        __ ?.r..
            traverseInorder(?.r..;

    ___ rotateRight node

        print("Rotating to the right on node ", ?.data);

        tempLeftChild _ ?.l..;
        t _ tempLeftChild.r..;

        tempLeftChild.r.. _ node;
        ?.l.. _ t;

        ?.height _ m__(calcHeight(?.l.., calcHeight(?.r..)) + 1;
        tempLeftChild.height _ m__(calcHeight(tempLeftChild.l..,
                                   calcHeight(tempLeftChild.r..)) + 1;

        r_ tempLeftChild;

    ___ rotateLeft node

        print("Rotating to the left on node ", ?.data);

        tempRightChild _ ?.r..;
        t _ tempRightChild.l..;

        tempRightChild.l.. _ node;
        ?.r.. _ t;

        ?.height _ m__(calcHeight(?.l.., calcHeight(?.r..)) + 1;
        tempRightChild.height _ m__(calcHeight(tempRightChild.l..,
                                    calcHeight(tempRightChild.r..)) + 1;

        r_ tempRightChild;


avl _ AVL()
avl.i.. (10)
avl.i.. (20)
avl.i.. (5)
avl.i.. (6)
avl.i.. (15)
avl.remove(15)
avl.remove(20)
avl.traverse()
