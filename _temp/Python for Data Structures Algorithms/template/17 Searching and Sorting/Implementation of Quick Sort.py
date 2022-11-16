# Implementation of Quick Sort
# A quick sort first selects a value, which is called the pivot value. Although there are many different ways to choose
# the pivot value, we will simply use the first item in the list. The role of the pivot value is to assist with
# splitting the list. The actual position where the pivot value belongs in the final sorted list, commonly called
# the split point, will be used to divide the list for subsequent calls to the quick sort.
# Resources for Review
# Check out the resources below for a review of Insertion sort!
#     Wikipedia
#     Visual Algo
#     Sorting Algorithms Animcation with Pseudocode

___ quick_sort(arr

    quick_sort_help(arr,0,l..(arr)-1)

___ quick_sort_help(arr,first,last

    __ first<last:


        splitpoint _ partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)


___ partition(arr,first,last

    pivotvalue _ arr[first]

    leftmark _ first+1
    rightmark _ last

    done _ F..
    _____ n.. done:

        _____ leftmark <_ rightmark ___ arr[leftmark] <_ pivotvalue:
            leftmark _ leftmark + 1

        _____ arr[rightmark] >_ pivotvalue ___ rightmark >_ leftmark:
            rightmark _ rightmark -1

        __ rightmark < leftmark:
            done _ T..
        ____
            temp _ arr[leftmark]
            arr[leftmark] _ arr[rightmark]
            arr[rightmark] _ temp

    temp _ arr[first]
    arr[first] _ arr[rightmark]
    arr[rightmark] _ temp


    r_ rightmark

arr _ [2,5,4,6,7,3,1,4,12,11]
quick_sort(arr)
arr
# [1, 2, 3, 4, 4, 5, 6, 7, 11, 12]
#
# Good Job!