#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

import QueueLinkedList as queue

c_ AVLNode:
    ___ -  data
        data _ data
        leftChild _ N..
        rightChild _ N..
        height _ 1

___ preOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

___ inOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

___ postOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
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
            __ root.value.leftChild __ n.. N..:
                customQueue.enqueue(root.value.leftChild)
            __ root.value.rightChild __ n.. N..:
                customQueue.enqueue(root.value.rightChild)


___ searchNode(rootNode, nodeValue
    __ rootNode.data __ nodeValue:
        print("The value is found")
    ____ nodeValue < rootNode.data:
        __ rootNode.leftChild.data __ nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.leftChild, nodeValue)
    ____
        __ rootNode.rightChild.data __ nodeValue:
            print("The value is found")
        ____
            searchNode(rootNode.rightChild, nodeValue)

___ getHeight(rootNode
    __ n.. rootNode:
        r_ 0
    r_ rootNode.height

___ rightRotate(disbalanceNode
    newRoot _ disbalanceNode.leftChild
    disbalanceNode.leftChild _ disbalanceNode.leftChild.rightChild
    newRoot.rightChild _ disbalanceNode
    disbalanceNode.height _ 1 + m__(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height _ 1 + m__(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    r_ newRoot

___ leftRotate(disbalanceNode
    newRoot _ disbalanceNode.rightChild
    disbalanceNode.rightChild _ disbalanceNode.rightChild.leftChild
    newRoot.leftChild _ disbalanceNode
    disbalanceNode.height _ 1 + m__(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height _ 1 + m__(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    r_ newRoot

___ getBalance(rootNode
    __ n.. rootNode:
        r_ 0
    r_ getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

___ insertNode(rootNode, nodeValue
    __ n.. rootNode:
        r_ AVLNode(nodeValue)
    ____ nodeValue < rootNode.data:
        rootNode.leftChild _ insertNode(rootNode.leftChild, nodeValue)
    ____
        rootNode.rightChild _ insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height _ 1 + m__(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance _ getBalance(rootNode)
    __ balance > 1 ___ nodeValue < rootNode.leftChild.data:
        r_ rightRotate(rootNode)
    __ balance > 1 ___ nodeValue > rootNode.leftChild.data:
        rootNode.leftChild _ leftRotate(rootNode.leftChild)
        r_ rightRotate(rootNode)
    __ balance < -1 ___ nodeValue > rootNode.rightChild.data:
        r_ leftRotate(rootNode)
    __ balance < -1 ___ nodeValue < rootNode.rightChild.data:
        rootNode.rightChild _ rightRotate(rootNode.rightChild)
        r_ leftRotate(rootNode)
    r_ rootNode

___ getMinValueNode(rootNode
    __ rootNode __ N.. __ rootNode.leftChild __ N..:
        r_ rootNode
    r_ getMinValueNode(rootNode.leftChild)

___ deleteNode(rootNode, nodeValue
    __ n.. rootNode:
        r_ rootNode
    ____ nodeValue < rootNode.data:
        rootNode.leftChild _ deleteNode(rootNode.leftChild, nodeValue)
    ____ nodeValue > rootNode.data:
        rootNode.rightChild _ deleteNode(rootNode.rightChild, nodeValue)
    ____
        __ rootNode.leftChild __ N..:
            temp _ rootNode.rightChild
            rootNode _ N..
            r_ temp
        ____ rootNode.rightChild __ N..:
            temp _ rootNode.leftChild
            rootNode _ N..
            r_ temp
        temp _ getMinValueNode(rootNode.rightChild)
        rootNode.data _ ?.data
        rootNode.rightChild _ deleteNode(rootNode.rightChild, ?.data)
    balance _ getBalance(rootNode)
    __ balance > 1 ___ getBalance(rootNode.leftChild) >_ 0:
        r_ rightRotate(rootNode)
    __ balance < -1 ___ getBalance(rootNode.rightChild) <_ 0:
        r_ leftRotate(rootNode)
    __ balance > 1 ___ getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild _ leftRotate(rootNode.leftChild)
        r_ rightRotate(rootNode)
    __ balance < -1 ___ getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild _ rightRotate(rootNode.rightChild)
        r_ leftRotate(rootNode)
    
    r_ rootNode

___ deleteAVL(rootNode
    rootNode.data _ N..
    rootNode.leftChild _ N..
    rootNode.rightChild _ N..
    r_ "The AVL has been successfully deleted"



newAVL _ AVLNode(5)
newAVL _ insertNode(newAVL, 10)
newAVL _ insertNode(newAVL, 15)
newAVL _ insertNode(newAVL, 20)
deleteAVL(newAVL)
levelOrderTraversal(newAVL)
