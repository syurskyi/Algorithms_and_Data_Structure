# The Binary Search Algorithm takes:
# data - A list or tuple.
# item - The item that you wish to find in the list (data).
def binary_search(data, item):

    # Set the initial bounds for the interval:
    # The lower bound is the first index in the list.
    # The upper bound is the last index in the list.
    low = 0
    high = len(data) - 1

    # While the interval is valid
    while low <= high:
        # Find the item in the middle of the interval
        middle = (low + high)//2
        # If that item is equal to the target item,
        # return the index.
        if data[middle] == item:
            return middle
        # If the item is not equal to the target item,
        # check if it's greater or smaller and reassign
        # the bounds appropriately. 
        elif data[middle] > item:
            high = middle - 1
        else:
            low = middle + 1

    # Else, if the item is not found in the list, return -1
    return -1
