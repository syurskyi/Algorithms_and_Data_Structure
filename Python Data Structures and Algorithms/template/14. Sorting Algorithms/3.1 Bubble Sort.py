def bubblesort(A):
    for i in range(len(A)-1, 0, - 1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


A = [84, 21, 96, 15, 47]
print('Originat Array: ', A)
bubblesort(A)
print('Sorted Array: ', A)

