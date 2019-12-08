def selection_sort(lst):
    # Traverse the list.
    # i represents the index where the unsorted portion of the list starts.
    for i in range(len(lst)):
        # The min_index variable describes the index of the
        # smallest element in the remaining unsorted array. 
        min_index = i
        # For each element in the unsorted portion of the list,
        # check if the element is smaller than the current min
        # and assign that index as the new min_index.
        for curr_index in range(i+1, len(lst)):
            if lst[min_index] > lst[curr_index]:
                min_index = curr_index
        # Swap the min element with the first element of the 
        # unsorted portion of the list.
        lst[i], lst[min_index] = lst[min_index], lst[i]
        
