#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ Heap:
    ___ -  size
        customList _ (size+1) * [N..]
        heapSize _ 0
        maxSize _ size + 1

___ peekofHeap(rootNode
    __ n.. rootNode:
        r_
    ____
        r_ rootNode.customList[1]

___ sizeofHeap(rootNode
    __ n.. rootNode:
        r_
    ____
        r_ rootNode.heapSize

___ levelOrderTraversal(rootNode
    __ n.. rootNode:
        r_
    ____
        ___ i __ range(1, rootNode.heapSize+1
            print(rootNode.customList[i])

___ heapifyTreeInsert(rootNode, index, heapType
    parentIndex _ int(index/2)
    __ index <_ 1:
        r_
    __ heapType __ "Min":
        __ rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp _ rootNode.customList[index]
            rootNode.customList[index] _ rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] _ temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType __ "Max":
        __ rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp _ rootNode.customList[index]
            rootNode.customList[index] _ rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] _ temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

___ inserNode(rootNode, nodeValue, heapType
    __ rootNode.heapSize + 1 __ rootNode.maxSize:
        r_ "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] _ nodeValue
    rootNode.heapSize +_ 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    r_ "The value has been successfully inserted"

___ heapifyTreeExtract(rootNode, index, heapType
    leftIndex _ index * 2
    rightIndex _ index * 2 + 1
    swapChild _ 0

    __ rootNode.heapSize < leftIndex:
        r_
    elif rootNode.heapSize __ leftIndex:
        __ heapType __ "Min":
            __ rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp _ rootNode.customList[index]
                rootNode.customList[index] _ rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] _ temp
            r_
        ____
            __ rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp _ rootNode.customList[index]
                rootNode.customList[index] _ rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] _ temp
            r_

    ____
        __ heapType __ "Min":
            __ rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild _ leftIndex
            ____
                swapChild _ rightIndex
            __ rootNode.customList[index] > rootNode.customList[swapChild]:
                temp _ rootNode.customList[index]
                rootNode.customList[index] _ rootNode.customList[swapChild]
                rootNode.customList[swapChild] _ temp
        ____
            __ rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild _ leftIndex
            ____
                swapChild _ rightIndex
            __ rootNode.customList[index] < rootNode.customList[swapChild]:
                temp _ rootNode.customList[index]
                rootNode.customList[index] _ rootNode.customList[swapChild]
                rootNode.customList[swapChild] _ temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

___ extractNode(rootNode, heapType
    __ rootNode.heapSize __ 0:
        r_
    ____
        extractedNode _ rootNode.customList[1]
        rootNode.customList[1] _ rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] _ N..
        rootNode.heapSize -_ 1
        heapifyTreeExtract(rootNode, 1, heapType)
        r_ extractedNode

___ deleteEntireBP(rootNode
    rootNode.customList _ N..








newHeap _ Heap(5)
inserNode(newHeap, 4, "Max")
inserNode(newHeap, 5, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")
deleteEntireBP(newHeap)
levelOrderTraversal(newHeap)


