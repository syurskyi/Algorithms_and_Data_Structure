# This recursive version of the Binary Search
# takes four parameters:
# data - the list or tuple
# low  - the lower bound
# high - the upper bound
# item - the item that you are looking for
def binary_search(data, low, high, item):
    # If the interval is valid
    if low <= high:
        # Find the middle of the list (index)
        middle = (low + high)//2
        # If the item in the middle of the list 
        # is the one that you are looking for, 
        # return the index.
        if data[middle] == item:
            return middle
        # Else, if it's greater than the item that you 
        # are looking for, make a recursive call passing
        # the middle index - 1 as upper bound to discard the
        # upper half of the list
        elif data[middle] > item:
            return binary_search(data, low, middle - 1, item)
        # Else, it it's smaller than the item that you 
        # are looking for, make a recursive call passing 
        # the middle index + 1 as lower bound to discard the 
        # lower half of the list.
        else:
            return binary_search(data, middle + 1, high, item)
    # If the item is not found, return -1
    else:
        return -1

