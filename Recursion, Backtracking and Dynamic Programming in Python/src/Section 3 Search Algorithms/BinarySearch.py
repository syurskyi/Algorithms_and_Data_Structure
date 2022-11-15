
def binary_search(container, item, left, right):

    # first base case - search misses
    if right < left:
        return -1

    # generate the index of the middle item
    middle_index = (left + right) // 2

    # we have found the item
    if container[middle_index] == item:
        return middle_index

    # have to check whether the middle_item is smaller or greater
    # the item is in the left sub-array
    elif container[middle_index] > item:
        print('Checking items on the left...')
        # we can discard the right side of the array (items greater than the middle item)
        return binary_search(container, item, left, middle_index-1)

    # the item is in the right sub-array
    elif container[middle_index] < item:
        print('Checking items on the right...')
        return binary_search(container, item, middle_index+1, right)


nums = [-5, -4, 0, 2, 4, 6, 8, 100, 500]
print(binary_search(nums, 2, 0, len(nums)-1))
