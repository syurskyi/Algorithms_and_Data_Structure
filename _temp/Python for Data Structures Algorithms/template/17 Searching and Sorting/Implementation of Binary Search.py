# Implementation of Binary Search
#
# In this notebook we will just implement two versions of a simple binary search. View the video lecture for
# a full breakdown!
# Binary Search

___ binary_search(arr,ele

    # First and last index values
    first _ 0
    last _ l..(arr) - 1

    found _ F..


    _____ first <_ last ___ n.. found:

        mid _ (first+last)/2 # or // for Python 3

        # Match found
        __ arr[mid] __ ele:
            f.. _ T..

        # Set new midpoints up or down depending on comparison
        ____
            # Set down
            __ ele < arr[mid]:
                last _ mid -1
            # Set up
            ____
                first _ mid + 1

    r_ found

# # list must already be sorted!
arr _ [1,2,3,4,5,6,7,8,9,10]

binary_search(arr,4)
# True
#
binary_search(arr,2.2)
# False
#
# Recursive Version of Binary Search

___ rec_bin_search(arr,ele

    # Base Case!
    __ l..(arr) __ 0:
        r_ F..

    # Recursive Case
    ____

        mid _ l..(arr)/2

        # If match found
        __ arr[mid]__ele:
            r_ T..

        ____

            # Call again on second half
            __ ele<arr[mid]:
                r_ rec_bin_search(arr[:mid],ele)

            # Or call on first half
            ____
                r_ rec_bin_search(arr[mid+1:],ele)

rec_bin_search(arr,3)
# True
#
rec_bin_search(arr,15)
# False
#
# Good Job!