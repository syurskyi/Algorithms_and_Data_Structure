def insertionsort(A):
    for i in range(1, len(A)):
        value = A[i]
        position = i

        while position > 0 and A[position - 1] > value:
            A[position] = A[position-1]
            position = position - 1
    A[position] = value


A = [84, 21, 96, 15, 47]
print('Originat Array: ', A)
insertionsort(A)
print('Sorted Array: ', A)
