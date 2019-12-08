def quicksort(lst, low, high):
    # If the interval [low, high] is valid
    if low < high: 
        # pivot_index is partitioning index,
        # lst[pivot_index] is now at the correct index 
        pivot_index = partition(lst, low, high) 
  
        # Sort the elements in the list
        # that come before and after the partition 
        quicksort(lst, low, pivot_index) 
        quicksort(lst, pivot_index+1, high)


# Using Hoare's Partition Scheme
def partition(lst, low, high):
    # Get the pivot element
    pivot = lst[low]
 
    # Get the indices that we will be working with
    i = low - 1
    j = high + 1

    # Indices move towards each other until they meet

    while True: 
        
        # Move the i index to the right until we
        # find an element that is smaller than the pivot. 
        i += 1
        while lst[i] < pivot:
            i += 1

        # Move the j index to the left until we find an element
        # that is greater than the pivot.
        j -= 1
        while lst[j] > pivot:
            j -= 1

        # If i and j did not meet before we need to make
        # a swap, then swap the elements
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
        # If j now comes before i in the list
        # (if no swaps were made before they crossed)
        # return the value of j.
        else:
            return j
