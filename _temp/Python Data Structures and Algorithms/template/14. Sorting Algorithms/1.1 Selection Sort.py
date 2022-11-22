___ selectionsort(A):
    for i in range(l..(A)-1, 0, - 1):
        max_position _ 0
        for j in range(1, i + 1):
            __ A[j] > A[max_position]:
                max_position _ j
        A[i], A[max_position] _ A[max_position], A[i]


A _ [84, 21, 96, 15, 47]
print('Original Array: ', A)
selectionsort(A)
print('Sorted Array: ', A)

