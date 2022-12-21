___ insertionSort(arr):
    ___ i __ r..(1, len(arr)):
        key = arr[i]
        last = i - 1

        ______ last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1

        arr[last + 1] = key


arr = [1, 2, 3, 4, 5]
insertionSort(arr)

print(arr)