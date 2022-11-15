
def linear_search(container, item):

    # the running time of this algorithms is O(N)
    # USE LINEAR SEARCH IF THE DATA STRUCTURE IS UNORDERED !!!

    for index in range(len(container)):
        if container[index] == item:
            # if we find the item: we return the index of that item
            return index

    # search miss - when the item is not present in the
    # underlying data structure (container)
    return -1


nums = [1, 5, -3, 10, 55, 100]
print(linear_search(nums, 10))
