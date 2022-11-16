___ insertionSort(arr
    ___ i __ range(1, l..(arr)):
        key _ arr[i]
        last _ i - 1

        _____ last >_ 0 and key < arr[last]:
            arr[last + 1] _ arr[last]
            last _ last - 1

        arr[last + 1] _ key


arr _ [1, 2, 3, 4, 5]
insertionSort(arr)

print(arr)