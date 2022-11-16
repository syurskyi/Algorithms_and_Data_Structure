# Implementation of Insertion Sort
#
# Insertion Sort builds the final sorted array (or list) one item at a time. It is much less efficient on large lists
# than more advanced algorithms such as quicksort, heapsort, or merge sort.
# Resources for Review
# Check out the resources below for a review of Insertion sort!
#     Wikipedia
#     Visual Algo
#     Animation
#     Sorting Algorithms Animcation with Pseudocode

___ insertion_sort(arr

    # For every index in array
    ___ i __ range(1,l..(arr)):

        # Set current values and position
        currentvalue _ arr[i]
        position _ i

        # Sorted Sublist
        _____ position>0 and arr[position-1]>currentvalue:

            arr[position]_arr[position-1]
            position _ position-1

        arr[position]_currentvalue

arr _[3,5,4,6,8,1,2,12,41,25]
insertion_sort(arr)
arr
# [1, 2, 3, 4, 5, 6, 8, 12, 25, 41]
#
# Good Job!