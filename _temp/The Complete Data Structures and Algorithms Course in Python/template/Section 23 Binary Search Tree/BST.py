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
    ____ nodeValue <_ rootNode.d..
        __ rootNode.l.. __ N..
            rootNode.l.. _ BSTNode(nodeValue)
        ____
            insertNode(rootNode.l.., nodeValue)
    ____
        __ rootNode.r.. __ N..
            rootNode.r.. _ BSTNode(nodeValue)
        ____
            insertNode(rootNode.r.., nodeValue)
    r_ "The node has been successfully inserted"

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


___ minValueNode(bstNode
    current _ bstNode
    _____ (current.l.. __ n.. N..
        current _ current.l..
    r_ current


___ deleteNode(rootNode, nodeValue
    __ rootNode __ N..
        r_ rootNode
    __ nodeValue < rootNode.d..
        rootNode.l.. _ deleteNode(rootNode.l.., nodeValue)
    ____ nodeValue > rootNode.d..
        rootNode.r.. _ deleteNode(rootNode.r.., nodeValue)
    ____
        __ rootNode.l.. __ N..
            temp _ rootNode.r..
            rootNode _ N..
            r_ temp
        
        __ rootNode.r.. __ N..
            temp _ rootNode.l..
            rootNode _ N..
            r_ temp
        
        temp _ minValueNode(rootNode.r..
        rootNode.data _ ?.data
        rootNode.r.. _ deleteNode(rootNode.r.., ?.data)
    r_ rootNode

___ deleteBST(rootNode
    rootNode.data _ N..
    rootNode.l.. _ N..
    rootNode.r.. _ N..
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

