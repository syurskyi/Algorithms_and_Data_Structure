def bubble_sort(lst):
    # Number of items in the list
    n = len(lst)
    
    # Traverse the list
    for i in range(n):
        # If the iteration causes a swap or not.
        # By default, it's False, but if a swap
        # occurs, it changes to True.
        swapped = False
            
        # For every unsorted element in the list
        # (the last i elements are already sorted)
        for j in range(0, n-i-1):
            # If the current element is greater than
            # the element to its right, swap them
            if lst[j] > lst[j+1]:
                # Swapping...
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # A swap occured, update the variable
                swapped = True
                
        # If the inner loop did not cause any swaps,
        # the list is sorted, so the loop can stop.
        if not swapped:
            break
