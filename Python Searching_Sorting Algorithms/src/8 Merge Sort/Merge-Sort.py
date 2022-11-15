def merge_sort(lst):
    
    # If the list is empty or it only contains one element
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        # Find the middle index
        middle_index = len(lst)//2

        # Call the function recursively
        # passing the left half and the right half
        # of the list in separate recursive calls
        left = merge_sort(lst[:middle_index])
        right = merge_sort(lst[middle_index:])

        # Returned the merged version of the
        # two halves already sorted in ascending order
        return merge(left, right)

# Merge the two halves
def merge(left_half, right_half):

    if not left_half or not right_half:
        return left_half or right_half
    
    result = []
    i, j = 0, 0

    while True:
        # If the element in the left half is smaller
        # than the element in the right half,
        # append that element to the result list 
        # at the current index.
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        # Else, if the element in the right half is smaller,
        # add that element to the list at the current index.
        else:
            result.append(right_half[j])
            j += 1

        # To check if there were any elements left
        # because the two halves may differ in length.
        # Insert the remaining elements to the list result.
        if i == len(left_half) or j == len(right_half):
            result.extend(left_half[i:] or right_half[j:])
            break

    return result

    
    
    
