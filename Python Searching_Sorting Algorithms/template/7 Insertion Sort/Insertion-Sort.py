def insertion_sort(lst):
    # For every element in the list (except the first one).
    for i in range(1, len(lst)):
        # Select the first element in the unsorted portion of the list.
        elem_selected = lst[i]

        # Check the elements in the unsorted portion
        # and move them one index to the right if they
        # are greater than the element selected.
        while i > 0 and elem_selected < lst[i-1]:
            lst[i] = lst[i-1]
            i -= 1

        # Insert the element where it belongs.
        lst[i] = elem_selected
            
        
