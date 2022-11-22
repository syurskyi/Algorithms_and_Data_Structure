def selectionsort(A):
    for i in range(len(A)-1, 0, - 1):
        max_position = 0
        for j in range(1, i + 1):
            if A[j] > A[max_position]:
                max_position = j
        A[i], A[max_position] = A[max_position], A[i]


A = [84, 21, 96, 15, 47]
print('Original Array: ', A)
selectionsort(A)
print('Sorted Array: ', A)

