#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

______ QueueLinkedList as queue

c_ BSTNode:
    ___ -  data
        ? _ ?
        leftChild _ N..
        rightChild _ N..

___ insertNode(rootNode, nodeValue
    __ rootNode.data __ N..
        rootNode.data _ nodeValue
    ____ nodeValue <_ rootNode.data:
        __ rootNode.leftChild __ N..
            rootNode.leftChild _ BSTNode(nodeValue)
        ____
            insertNode(rootNode.leftChild, nodeValue)
    ____
        __ rootNode.rightChild __ N..
            rootNode.rightChild _ BSTNode(nodeValue)
        ____
            insertNode(rootNode.rightChild, nodeValue)
    r_ "The node has been successfully inserted"

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
            __ root.value.leftChild __ n.. N..
                customQueue.enqueue(root.value.leftChild)
            __ root.value.rightChild __ n.. N..
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


___ minValueNode(bstNode
    current _ bstNode
    _____ (current.leftChild __ n.. N..
        current _ current.leftChild
    r_ current


___ deleteNode(rootNode, nodeValue
    __ rootNode __ N..
        r_ rootNode
    __ nodeValue < rootNode.data:
        rootNode.leftChild _ deleteNode(rootNode.leftChild, nodeValue)
    ____ nodeValue > rootNode.data:
        rootNode.rightChild _ deleteNode(rootNode.rightChild, nodeValue)
    ____
        __ rootNode.leftChild __ N..
            temp _ rootNode.rightChild
            rootNode _ N..
            r_ temp
        
        __ rootNode.rightChild __ N..
            temp _ rootNode.leftChild
            rootNode _ N..
            r_ temp
        
        temp _ minValueNode(rootNode.rightChild)
        rootNode.data _ ?.data
        rootNode.rightChild _ deleteNode(rootNode.rightChild, ?.data)
    r_ rootNode

___ deleteBST(rootNode
    rootNode.data _ N..
    rootNode.leftChild _ N..
    rootNode.rightChild _ N..
    r_ "The BST has been successfully deleted"



newBST _ BSTNode(N..)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
print(deleteBST(newBST))
levelOrderTraversal(newBST)

