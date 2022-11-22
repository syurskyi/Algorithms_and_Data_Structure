___ insertionsort(A):
    for i in range(1, l..(A)):
        value _ A[i]
        position _ i

        while position > 0 and A[position - 1] > value:
            A[position] _ A[position-1]
            position _ position - 1
    A[position] _ value


A _ [84, 21, 96, 15, 47]
print('Originat Array: ', A)
insertionsort(A)
print('Sorted Array: ', A)
