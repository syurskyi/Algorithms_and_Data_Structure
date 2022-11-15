# The Binary Search Algorithm takes:
# data - A list or tuple
# item - the target item that you wish to find in data
def binary_search(data, item):

    print("======> Starting Binary Search")

    # Set the initial bounds for the interval.
    # Lower bound is the first item in the list.
    # Upper bound is the last item in the list.

    low = 0
    high = len(data) - 1

    print("Initial bounds:")
    print("Lower bound:", low)
    print("Upper bound:", high)

    # Variables added for illustration purposes,
    # to count the number of iterations
    i = 0

    # While the interval is not empty
    while low <= high:
        print(f"\n=== Iteration #{i} ===")
        print("Lower bound:", low)
        print("Upper bound:", high)
        # Find the item in the middle of the interval
        middle = (low + high)//2
        print("Middle index:", middle)
        print("We are looking for:", item)
        print("The middle element is:", data[middle])
        # If that item is equal to the target item,
        # return the index.
        print("Is this the target item?", "True" if data[middle] == item else "No")
        if data[middle] == item:
            print("The item was found at index", middle)
            return middle
        # If the item is not equal to the target item,
        # check if it's larger or smaller and reassign
        # the bounds appropriately. 
        elif data[middle] > item:
                print("This middle element is greater than the target item:", data[middle], ">", item)
                print("We need to discard the upper half of the list")
                print("The lower bound remains at:", low)
                print("Now the new upper bound is:", middle - 1)
                high = middle - 1
        else:
                print("This middle item is smaller than the target item:", data[middle], "<", item)
                print("We need to discard the lower half of the list")
                print("Now the new lower bound is:", middle + 1)
                print("The upper bound remains at:", high)
                low = middle + 1
        i += 1

    # Else, if the item is not found in the list, return -1
    print("The target item was not found in the list")
    return -1
