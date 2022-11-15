import random

def quicksort(lst, low, high):
    # If the interval [low, high] is valid
    if low < high: 
        # Partition the list and get the partitioning index.
        pivot_index = random_pivot_partition(lst, low, high) 
  
        # Sort the elements in the list
        # that come before and after the partition 
        quicksort(lst, low, pivot_index-1) 
        quicksort(lst, pivot_index+1, high)

def random_pivot_partition(lst, low, high):
    # Generate a random index to select
    # an element randomly
    random_index = random.randrange(low, high)
    # Swap that random element with the last
    # element in the list (the element that would have
    # been used as the pivot). Now the random element
    # will be used as the pivot.
    lst[high], lst[random_index] = lst[random_index], lst[high]
    return partition(lst, low, high)

# Using Lomuto's Partition Scheme
def partition(lst, low, high):
    # Pivot
    pivot = lst[high]

    i = low - 1     
  
    for j in range(low, high): 
        # If the current element is smaller than
        # or equal to pivot 
        if lst[j] <= pivot: 
            # Increment index
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
             
    lst[i+1], lst[high] = lst[high], lst[i+1] 
    return i+1 
