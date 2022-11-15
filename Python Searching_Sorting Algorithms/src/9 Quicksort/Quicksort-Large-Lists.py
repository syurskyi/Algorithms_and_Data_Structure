import random

def quicksort(lst, low, high):
    # If the interval [low, high] is valid
    if low < high: 
        # Partition the list and get the partitioning index.
        pivot_index = partition(lst, low, high) 
  
        # Sort the elements in the list
        # that come before and after the partition 
        quicksort(lst, low, pivot_index-1) 
        quicksort(lst, pivot_index+1, high)

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


# Create a list with 100,000 items
a = [i for i in range(100000)]

# Shuffle the list
random.shuffle(a)
# Print the list before sorting
print("===================")
print("Before sorting:")
print(a)
print("Length:", len(a))

# Sort the list
quicksort(a, 0, len(a)-1)

# Print the sorted list
print("\n===================")
print("After sorting:")
print(a)
print("===================")
