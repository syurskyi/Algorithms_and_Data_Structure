def quicksort(lst, low, high):

    print("\n=======> Starting quicksort()")
    print("List:", lst)
    print("Low (index):", low)
    print("High (index):", high)

    print(f"Is the interval [{low}, {high}] valid (has more than 1 element)?", "Yes" if low < high else "No")
        
    # If the interval [low, high] is valid
    if low < high:
        
        # Partition the list and get the partitioning index.
        pivot_index = partition(lst, low, high)

        print("\n-> Back to quicksort()\n")
        print("The pivot index is:", pivot_index)
  
        # Sort the elements in the list
        # that come before and after the partition

        print("Calling quicksort() recursively passing:")
        print("List:", lst)
        print("Low:", low)
        print("High:", pivot_index-1)
        
        quicksort(lst, low, pivot_index-1)

        print("\n-> Back to quicksort()\n")

        print("Calling quicksort() recursively passing:")
        print("List:", lst)
        print("Low:", pivot_index+1)
        print("High:", high)
        
        quicksort(lst, pivot_index+1, high)
    else:
        print("This part of the recursive process stops.")
    
# Using Lomuto's Partition Scheme
def partition(lst, low, high):

    print("\n---> Entering partition()")
    
    # Pivot
    pivot = lst[high]

    print("The pivot is the element:", pivot)
    print("Located at index:", high)

    i = low - 1

    print("i is initialized to:", i)
  
    print("\n-> Starting the For loop")

    for j in range(low, high):

        print("\nValue of j:", j)
        print(f"Is the current element lst[{j}] ({lst[j]}) <= to the pivot ({pivot})?")
        print("Yes, it is!" if  lst[j] <= pivot else "No, it isn't! We don't need to make any changes")
        
        # If the current element is smaller than
        # or equal to pivot 
        if lst[j] <= pivot: 
            # Increment index
            print("\nSo we need to increment the value of i")
            print("Old value of i:", i)
            i += 1
            print("New value of i:", i)

            print(f"\nAnd we need to swap the element at index i (index {i}):", lst[i])
            print(f"with the element at index j (index {j}):", lst[j])
            print("\nSwapping...")
            print("Old list:", lst)
            lst[i], lst[j] = lst[j], lst[i]
            print("New list:", lst)
            print("Swap completed")

    # Put the pivot where it should be
    # at index i+1 by swapping it with that element
    print("\n--> Out of the for loop")
    
    print(f"\nNow we need to move the pivot to index i+1 (index {i+1})")
    
    print("\nSwapping...")
    print(f"Swapping the pivot ({lst[high]}) with the element at index {i+1} ({lst[i+1]})")
    print("\nOld list:", lst)
    lst[i+1], lst[high] = lst[high], lst[i+1]
    print("New list:", lst)
    print("Swap completed!")
    
    print(f"\nReturning the index of the pivot element after the swap: {i+1}")
    print("\nThis generates a partition of the list:")
    print("List:", lst)
    print("Left sublist:", lst[low:i+1], "where all the elements are smaller than the pivot.")
    print("Right sublist:", lst[i+2:high+1], "where all the elements are greater than the pivot.")
    print("The pivot element is in the middle.")

    print("\nPartition Completed!")
    return i+1 
