# Binary Heap Implementation
#
# Here is the reference code for the Binary Heap Implementation. Make sure to refer to the video lecture for the full
# explanation!
# Binary Heap Operations
#
# The basic operations we will implement for our binary heap are as follows:
#
#     BinaryHeap() creates a new, empty, binary heap.
#     insert(k) adds a new item to the heap.
#     findMin() returns the item with the minimum key value, leaving item in the heap.
#     delMin() returns the item with the minimum key value, removing the item from the heap.
#     isEmpty() returns true if the heap is empty, false otherwise.
#     size() returns the number of items in the heap.
#     buildHeap(list) builds a new heap from a list of keys.

c_ BinHeap:
    ___ -  
        heapList _ [0]
        currentSize _ 0

    ___ percUpi

        _____ i // 2 > 0:


            __ heapList[i] < heapList[i // 2]:

                tmp _ heapList[i // 2]
                heapList[i // 2] _ heapList[i]
                heapList[i] _ tmp
            i _ i // 2

    ___ insertk

        heapList.append(k)
        currentSize _ currentSize + 1
        percUp(currentSize)

    ___ percDowni

        _____ (i * 2) <_ currentSize:

            mc _ minChild(i)
            __ heapList[i] > heapList[mc]:

                tmp _ heapList[i]
                heapList[i] _ heapList[mc]
                heapList[mc] _ tmp
            i _ mc

    ___ minChildi

        __ i * 2 + 1 > currentSize:

            r_ i * 2
        ____

            __ heapList[i*2] < heapList[i*2+1]:
                r_ i * 2
            ____
                r_ i * 2 + 1

    ___ delMin 
        retval _ heapList[1]
        heapList[1] _ heapList[currentSize]
        currentSize _ currentSize - 1
        heapList.pop()
        percDown(1)
        r_ retval

    ___ buildHeapalist
        i _ len(alist) // 2
        currentSize _ len(alist)
        heapList _ [0] + alist[:]
        _____ (i > 0
            percDown(i)
            i _ i - 1