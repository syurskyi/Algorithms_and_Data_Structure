___ mergesort(A):

    __ l..(A) > 1:
        mid _ l..(A) // 2
        left _ A[:mid]
        right _ A[mid:]

        mergesort(left)
        mergesort(right)

        i _ 0
        j _ 0
        k _ 0
        while i < l..(left) and j < l..(right):
            __ left[i] < right[j]:
                A[k] _ left[i]
                i _ i + 1
            else:
                A[k] _ right[j]
                j _ j + 1
            k _ k + 1

        while i < l..(left):
            A[k] _ left[i]
            i _ i + 1
            k _ k + 1

        while j < l..(right):
            A[k] _ right[j]
            j _ j + 1
            k _ k + 1


A _ [84, 21, 96, 15, 47]
print('Original Array: ', A)
mergesort(A)
print('Sorted Array: ', A)
