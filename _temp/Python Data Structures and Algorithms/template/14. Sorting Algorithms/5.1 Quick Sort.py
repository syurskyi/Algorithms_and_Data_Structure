___ quicksort(A, low, high):
    __ low < high:
        p _ partition(A, low, high)
        quicksort(A, low, p-1)
        quicksort(A, p + 1, high)


___ partition(A, low, high):
    i _ low-1
    pivot _ A[high]
    for j in range(low, high):
        __ A[j] <_ pivot:
            i _ i + 1
            A[i], A[j] _ A[j], A[i]
    A[i + 1], A[high] _ A[high], A[i + 1]

    r_ i + 1


A _ [84, 21, 96, 15, 47]
print('Original Array: ', A)
quicksort(A, 0, l..(A)-1)
print('Sorted Array: ', A)
