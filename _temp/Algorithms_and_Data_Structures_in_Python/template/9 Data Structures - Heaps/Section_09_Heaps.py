c_ Heap o..
    HEAP_SIZE _ 10

    ___ -
        heap _ [0] * Heap.HEAP_SIZE
        currentPosition _ -1

    ___ insert item

        __ isFull(
            print("Heap is full..");
            r_

        currentPosition _ currentPosition + 1
        heap[currentPosition] _ item
        fixUp(currentPosition)

    ___ fixUp index

        parentIndex _ int((index - 1) / 2)

        _____ parentIndex >_ 0 and heap[parentIndex] < heap[index]:
            temp _ heap[index]
            heap[index] _ heap[parentIndex]
            heap[parentIndex] _ temp
            index _ parentIndex
            parentIndex _ (int)((index - 1) / 2)

    ___ heapsort

        ___ i __ range(0, currentPosition + 1
            temp _ heap[0]
            print("%d " % temp)
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
                    break

                index _ childToSwap
            ____
                break;

    ___ isFull
        __ currentPosition == Heap.HEAP_SIZE:
            r_ True
        ____
            r_ False


__ __name__ == "__main__":
    heap _ Heap()
    heap.insert(10)
    heap.insert(-20)
    heap.insert(0)
    heap.insert(2)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(20)
    heap.insert(15)

    heap.heapsort()
