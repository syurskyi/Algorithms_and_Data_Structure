def binary_search(data, low, high, item):

    print("\n===> Calling Binary Search")
    print("Lower bound:", low)
    print("Upper bound:", high)

    if low <= high:
        middle = (low + high)//2
        print("Middle index:", middle)
        print("Item at middle index:", data[middle])
        print("We are looking for:", item)
        print("Is this the item?", "Yes" if data[middle] == item else "No")
        if data[middle] == item:
            print("The item was found at index:", middle)
            return middle
        elif data[middle] > item:
            print("The current item is greater than the target item:", data[middle], ">", item)
            print("We need to discard the upper half of the list")
            print("The lower bound remains at:", low)
            print("The upper bound is now:", middle - 1)
            return binary_search(data, low, middle - 1, item)
        else:
            print("The current item is smaller than the target item:", data[middle], "<", item)
            print("We need to discard the lower half of the list")
            print("The lower bound is now:", middle + 1)
            print("The upper bound remains at:", high)
            return binary_search(data, middle + 1, high, item)
    else:
        print("The item was not found in the list")
        return -1
