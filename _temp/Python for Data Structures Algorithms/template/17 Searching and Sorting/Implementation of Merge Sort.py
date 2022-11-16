# Implementation of Merge Sort
# Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
# Resources for Review
# Check out the resources below for a review of Merge sort!
#     Wikipedia
#     Visual Algo
#     Sorting Algorithms Animcation with Pseudocode

___ merge_sort(arr

    __ l..(arr)>1:
        mid _ l..(arr)/2
        lefthalf _ arr[:mid]
        righthalf _ arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i_0
        j_0
        k_0
        _____ i < l..(lefthalf) and j < l..(righthalf
            __ lefthalf[i] < righthalf[j]:
                arr[k]_lefthalf[i]
                i_i+1
            ____
                arr[k]_righthalf[j]
                j_j+1
            k_k+1

        _____ i < l..(lefthalf
            arr[k]_lefthalf[i]
            i_i+1
            k_k+1

        _____ j < l..(righthalf
            arr[k]_righthalf[j]
            j_j+1
            k_k+1

arr _ [11,2,5,4,7,6,8,1,23]
merge_sort(arr)
arr
# [1, 2, 4, 5, 6, 7, 8, 11, 23]
#
# Good Job!