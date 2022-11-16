# Implementation of a Bubble Sort
#
# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of
# order. Each pass through the list places the next largest value in its proper place. In essence, each item bubbles
# up to the location where it belongs.
# Resources for Review
#
# Check out the resources below for a review of Bubble sort!
#
#     Wikipedia
#     Visual Algo
#     Animation
#     Sorting Algorithms Animcation with Pseudocode

___ bubble_sort(arr
    # For every element (arranged backwards)
    ___ n __ range(l..(arr)-1,0,-1
        #
        ___ k __ range(n
            # If we come to a point to switch
            __ arr[k]>arr[k+1]:
                temp _ arr[k]
                arr[k] _ arr[k+1]
                arr[k+1] _ temp

arr _ [3,2,13,4,6,5,7,8,1,20]
bubble_sort(arr)

arr
# [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
#
# Great Job!