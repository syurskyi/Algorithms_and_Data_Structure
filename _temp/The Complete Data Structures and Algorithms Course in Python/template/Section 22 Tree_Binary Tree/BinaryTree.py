#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

import QueueLinkedList as queue

c_ TreeNode:
    ___ -  data
        data _ data
        leftChild _ N..
        rightChild _ N..

newBT _ TreeNode("Drinks")
leftChild _ TreeNode("Hot")
tea _ TreeNode("Tea")
coffee _ TreeNode("Coffee")
leftChild.leftChild _ tea
leftChild.rightChild _ coffee
rightChild _ TreeNode("Cold")
newBT.leftChild _ leftChild
newBT.rightChild _ rightChild

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
        _____ n..(customQueue.isEmpty()):
            root _ customQueue.dequeue()
            print(root.value.data)
            __ (root.value.leftChild __ n.. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ n.. N..
                customQueue.enqueue(root.value.rightChild)

___ searchBT(rootNode, nodeValue
    __ n.. rootNode:
        r_ "The BT does not exist"
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty()):
            root _ customQueue.dequeue()
            __ root.value.data __ nodeValue:
                r_ "Success"
            __ (root.value.leftChild __ n.. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ n.. N..
                customQueue.enqueue(root.value.rightChild)
        r_ "Not found"

___ insertNodeBT(rootNode, newNode
    __ n.. rootNode:
        rootNode _ newNode
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty()):
            root _ customQueue.dequeue()
            __ root.value.leftChild __ n.. N..:
                customQueue.enqueue(root.value.leftChild)
            ____
                root.value.leftChild _ newNode
                r_ "Successfully Inserted"
            __ root.value.rightChild __ n.. N..:
                customQueue.enqueue(root.value.rightChild)
            ____
                root.value.rightChild _ newNode
                r_ "Successfully Inserted"

___ getDeepestNode(rootNode
    __ n.. rootNode:
        r_
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty()):
            root _ customQueue.dequeue()
            __ (root.value.leftChild __ n.. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ n.. N..
                customQueue.enqueue(root.value.rightChild)
        deepestNode _ root.value
        r_ deepestNode

___ deleteDeepestNode(rootNode, dNode
    __ n.. rootNode:
        r_
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty()):
            root _ customQueue.dequeue()
            __ root.value __ dNode:
                root.value _ N..
                r_
            __ root.value.rightChild:
                __ root.value.rightChild __ dNode:
                    root.value.rightChild _ N..
                    r_
                ____
                    customQueue.enqueue(root.value.rightChild)
            __ root.value.leftChild:
                __ root.value.leftChild __ dNode:
                    root.value.leftChild _ N..
                    r_
                ____
                    customQueue.enqueue(root.value.leftChild)

___ deleteNodeBT(rootNode, node
    __ n.. rootNode:
        r_ "The BT does not exist"
    ____
        customQueue _ queue.Queue()
        customQueue.enqueue(rootNode)
        _____ n..(customQueue.isEmpty()):
            root _ customQueue.dequeue()
            __ root.value.data __ node:
                dNode _ getDeepestNode(rootNode)
                root.value.data _ dNode.data
                deleteDeepestNode(rootNode, dNode)
                r_ "The node has been successfully deleted"
            __ (root.value.leftChild __ n.. N..
                customQueue.enqueue(root.value.leftChild)
            
            __ (root.value.rightChild __ n.. N..
                customQueue.enqueue(root.value.rightChild)
        r_ "Failed to delete"

___ deleteBT(rootNode
    rootNode.data _ N..
    rootNode.leftChild _ N..
    rootNode.rightChild _ N..
    r_ "The BT has been successfully deleted"

inOrderTraversal(newBT)

        
            





