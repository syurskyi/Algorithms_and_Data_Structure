#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

______ QueueLinkedList as queue

c_ AVLNode:
    ___ -  data
        ? _ ?
        leftChild _ N..
        rightChild _ N..
        height _ 1

___ preOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    print(rootNode.data)
    preOrderTraversal(rootNode.l..
    preOrderTraversal(rootNode.r..

___ inOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    inOrderTraversal(rootNode.l..
    print(rootNode.data)
    inOrderTraversal(rootNode.r..

___ postOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    postOrderTraversal(rootNode.l..
    postOrderTraversal(rootNode.r..
    print(rootNode.data)

___ levelOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty(
            root _ customQueue.dequeue()
            print(root.value.data)
            __ root.value.l.. __ n.. N..
                customQueue.enqueue(root.value.l..
            __ root.value.r.. __ n.. N..
                customQueue.enqueue(root.value.r..


___ searchNode(rootNode, nodeValue
    __ rootNode.data __ nodeValue:
        print("The value is found")
    ____ nodeValue < rootNode.d..
        __ rootNode.l...data __ nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.l.., nodeValue)
    ____
        __ rootNode.r...data __ nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.r.., nodeValue)

___ getHeight(rootNode
    __ n.. rootNode:
        r_ 0
    r_ rootNode.height

___ rightRotate(disbalanceNode
    newRoot _ disbalanceNode.l..
    disbalanceNode.l.. _ disbalanceNode.l...rightChild
    newRoot.r.. _ disbalanceNode
    disbalanceNode.height _ 1 + m__(getHeight(disbalanceNode.l.., getHeight(disbalanceNode.r..))
    newRoot.height _ 1 + m__(getHeight(newRoot.l.., getHeight(newRoot.r..))
    r_ newRoot

___ leftRotate(disbalanceNode
    newRoot _ disbalanceNode.r..
    disbalanceNode.r.. _ disbalanceNode.r...l..
    newRoot.l.. _ disbalanceNode
    disbalanceNode.height _ 1 + m__(getHeight(disbalanceNode.l.., getHeight(disbalanceNode.r..))
    newRoot.height _ 1 + m__(getHeight(newRoot.l.., getHeight(newRoot.r..))
    r_ newRoot

___ getBalance(rootNode
    __ n.. rootNode:
        r_ 0
    r_ getHeight(rootNode.l.. - getHeight(rootNode.r..

___ insertNode(rootNode, nodeValue
    __ n.. rootNode:
        r_ AVLNode(nodeValue)
    ____ nodeValue < rootNode.d..
        rootNode.l.. _ insertNode(rootNode.l.., nodeValue)
    ____
        rootNode.r.. _ insertNode(rootNode.r.., nodeValue)
    
    rootNode.height _ 1 + m__(getHeight(rootNode.l.., getHeight(rootNode.r..))
    balance _ getBalance(rootNode)
    __ balance > 1 ___ nodeValue < rootNode.l...data:
        r_ rightRotate(rootNode)
    __ balance > 1 ___ nodeValue > rootNode.l...data:
        rootNode.l.. _ leftRotate(rootNode.l..
        r_ rightRotate(rootNode)
    __ balance < -1 ___ nodeValue > rootNode.r...data:
        r_ leftRotate(rootNode)
    __ balance < -1 ___ nodeValue < rootNode.r...data:
        rootNode.r.. _ rightRotate(rootNode.r..
        r_ leftRotate(rootNode)
    r_ rootNode

___ getMinValueNode(rootNode
    __ rootNode __ N.. __ rootNode.l.. __ N..
        r_ rootNode
    r_ getMinValueNode(rootNode.l..

___ deleteNode(rootNode, nodeValue
    __ n.. rootNode:
        r_ rootNode
    ____ nodeValue < rootNode.d..
        rootNode.l.. _ deleteNode(rootNode.l.., nodeValue)
    ____ nodeValue > rootNode.d..
        rootNode.r.. _ deleteNode(rootNode.r.., nodeValue)
    ____
        __ rootNode.l.. __ N..
            temp _ rootNode.r..
            rootNode _ N..
            r_ temp
        ____ rootNode.r.. __ N..
            temp _ rootNode.l..
            rootNode _ N..
            r_ temp
        temp _ getMinValueNode(rootNode.r..
        rootNode.data _ ?.data
        rootNode.r.. _ deleteNode(rootNode.r.., ?.data)
    balance _ getBalance(rootNode)
    __ balance > 1 ___ getBalance(rootNode.l.. >_ 0:
        r_ rightRotate(rootNode)
    __ balance < -1 ___ getBalance(rootNode.r.. <_ 0:
        r_ leftRotate(rootNode)
    __ balance > 1 ___ getBalance(rootNode.l.. < 0:
        rootNode.l.. _ leftRotate(rootNode.l..
        r_ rightRotate(rootNode)
    __ balance < -1 ___ getBalance(rootNode.r.. > 0:
        rootNode.r.. _ rightRotate(rootNode.r..
        r_ leftRotate(rootNode)
    
    r_ rootNode

___ deleteAVL(rootNode
    rootNode.data _ N..
    rootNode.l.. _ N..
    rootNode.r.. _ N..
    r_ "The AVL has been successfully deleted"



newAVL _ AVLNode(5)
newAVL _ insertNode(newAVL, 10)
newAVL _ insertNode(newAVL, 15)
newAVL _ insertNode(newAVL, 20)
deleteAVL(newAVL)
levelOrderTraversal(newAVL)
