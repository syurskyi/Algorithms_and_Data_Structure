#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

______ QueueLinkedList as queue

c_ TreeNode:
    ___ -  data
        ? _ ?
        leftChild _ N..
        rightChild _ N..

newBT _ TreeNode("Drinks")
leftChild _ TreeNode("Hot")
tea _ TreeNode("Tea")
coffee _ TreeNode("Coffee")
leftChild.l.. _ tea
leftChild.r.. _ coffee
rightChild _ TreeNode("Cold")
newBT.l.. _ leftChild
newBT.r.. _ rightChild

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
            __ (root.value.l.. __ n.. N..
                customQueue.enqueue(root.value.l..
            
            __ (root.value.r.. __ n.. N..
                customQueue.enqueue(root.value.r..

___ searchBT(rootNode, nodeValue
    __ n.. rootNode:
        r_ "The BT does not exist"
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty(
            root _ customQueue.dequeue()
            __ root.value.data __ nodeValue:
                r_ "Success"
            __ (root.value.l.. __ n.. N..
                customQueue.enqueue(root.value.l..
            
            __ (root.value.r.. __ n.. N..
                customQueue.enqueue(root.value.r..
        r_ "Not found"

___ insertNodeBT(rootNode, newNode
    __ n.. rootNode:
        rootNode _ newNode
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty(
            root _ customQueue.dequeue()
            __ root.value.l.. __ n.. N..
                customQueue.enqueue(root.value.l..
            ____
                root.value.l.. _ newNode
                r_ "Successfully Inserted"
            __ root.value.r.. __ n.. N..
                customQueue.enqueue(root.value.r..
            ____
                root.value.r.. _ newNode
                r_ "Successfully Inserted"

___ getDeepestNode(rootNode
    __ n.. rootNode:
        r_
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty(
            root _ customQueue.dequeue()
            __ (root.value.l.. __ n.. N..
                customQueue.enqueue(root.value.l..
            
            __ (root.value.r.. __ n.. N..
                customQueue.enqueue(root.value.r..
        deepestNode _ root.value
        r_ deepestNode

___ deleteDeepestNode(rootNode, dNode
    __ n.. rootNode:
        r_
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty(
            root _ customQueue.dequeue()
            __ root.value __ dNode:
                root.value _ N..
                r_
            __ root.value.r..
                __ root.value.r.. __ dNode:
                    root.value.r.. _ N..
                    r_
                ____
                    customQueue.enqueue(root.value.r..
            __ root.value.l..
                __ root.value.l.. __ dNode:
                    root.value.l.. _ N..
                    r_
                ____
                    customQueue.enqueue(root.value.l..

___ deleteNodeBT(rootNode, node
    __ n.. rootNode:
        r_ "The BT does not exist"
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty(
            root _ customQueue.dequeue()
            __ root.value.data __ node:
                dNode _ getDeepestNode(rootNode)
                root.value.data _ dNode.data
                deleteDeepestNode(rootNode, dNode)
                r_ "The node has been successfully deleted"
            __ (root.value.l.. __ n.. N..
                customQueue.enqueue(root.value.l..
            
            __ (root.value.r.. __ n.. N..
                customQueue.enqueue(root.value.r..
        r_ "Failed to delete"

___ deleteBT(rootNode
    rootNode.data _ N..
    rootNode.l.. _ N..
    rootNode.r.. _ N..
    r_ "The BT has been successfully deleted"

inOrderTraversal(newBT)

        
            





