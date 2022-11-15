def linear_search_recursive(container, item, index=0):
    # base case for search miss (when item is not present in the container)
    if index >= len(container):
        return -1

    # base case when we find the item
    if container[index] == item:
        return index

    return linear_search_recursive(container, item, index + 1)


nums = [1, 4, 6, -4, 0, 100]
print(linear_search_recursive(nums, 0))