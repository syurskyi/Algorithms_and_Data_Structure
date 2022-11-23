c_ Heap o..
    HEAP_SIZE _ 10

    ___ -
        heap _ [0] * Heap.HEAP_SIZE
        currentPosition _ -1

    ___ i..  item

        __ isFull(
            print("Heap is full..");
            r_

        currentPosition _ currentPosition + 1
        heap[currentPosition] _ item
        fixUp(currentPosition)

    ___ fixUp index

        parentIndex _ i..((index - 1) / 2)

        _____ parentIndex >_ 0 ___ heap[parentIndex] < heap[index]:
            temp _ heap[index]
            heap[index] _ heap[parentIndex]
            heap[parentIndex] _ temp
            index _ parentIndex
            parentIndex _ (i..)((index - 1) / 2)

    ___ heapsort

        ___ i __ r..(0, currentPosition + 1
            temp _ heap[0]
            print("%d " _ temp)
            heap[0] _ heap[currentPosition - i]
            heap[currentPosition - i] _ temp
            fixDown(0, currentPosition - i - 1)

    ___ fixDown index, upto

        _____ index <_ upto:

            leftChild _ 2 * index + 1
            rightChild _ 2 * index + 2

            __ leftChild < upto:
                childToSwap _ N..

                __ rightChild > upto:
                    childToSwap _ leftChild
                ____
                    __ heap[leftChild] > heap[rightChild]:
                        childToSwap _ leftChild
                    ____
                        childToSwap _ rightChild

                __ heap[index] < heap[childToSwap]:
                    temp _ heap[index]
                    heap[index] _ heap[childToSwap]
                    heap[childToSwap] _ temp
                ____
                    b..

                index _ childToSwap
            ____
                b..;

    ___ isFull
        __ currentPosition __ Heap.HEAP_SIZE:
            r_ T..
        ____
            r_ F..


__ __name__ __ "__main__":
    heap _ Heap()
    heap.i.. (10)
    heap.i.. (-20)
    heap.i.. (0)
    heap.i.. (2)
    heap.i.. (4)
    heap.i.. (5)
    heap.i.. (6)
    heap.i.. (7)
    heap.i.. (20)
    heap.i.. (15)

    heap.heapsort()
