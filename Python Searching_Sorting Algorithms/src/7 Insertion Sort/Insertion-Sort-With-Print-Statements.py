def insertion_sort(lst):

    print("\n=========> Starting Insertion Sort")

    for i in range(1, len(lst)):

        print(f"\n---> Outer loop. Iteration #{i} (i = {i})")

        if i <= len(lst) - 1:
            print("Sorted portion:", lst[:i])
            print("Unsorted portion:", lst[i:])
        else:
            print("The list is completely sorted!")
            print(lst)
  
        elem_selected = lst[i]

        print(f"\nWe need to find the correct spot for: {elem_selected}.")
        print(f"{elem_selected} is the first element in the unsorted portion.")
        print(f"Now let's compare {elem_selected} with the elements of the sorted portion.")
        print("Let's find where it belongs...")

        # Move all the elements from the sorted portion of the list
        # one index to the right if they are greater
        # than the element selected.
        
        while i > 0 and elem_selected < lst[i-1]:
            print("\n-> Inner loop")
            print(f"Is the element selected {elem_selected} smaller than {lst[i-1]}?")
            print(f"Yes, it is! So we need to move {lst[i-1]} to the right to make room for {elem_selected}")
            print(f"Moving {lst[i-1]} from index {i-1} to index {i} (see below)")
            print("Old list:", lst)
            lst[i] = lst[i-1]
            print("New list:", lst)
            print(f"See how {lst[i-1]} is now at index {i}")
            i -= 1

        if i > 0 and elem_selected >= lst[i-1]:
            print(f"\nIs the element selected ({elem_selected}) smaller than {lst[i-1]}?")
            print(f"No, it isn't! We need to stay where we are, at index {i}.")
            print(f"The element {elem_selected} should be there.")

        # Place the element where it belongs
        print("\nBingo!")
        print(f"We've found the right location for {elem_selected}: index {i}")
        lst[i] = elem_selected
        print("The list is now:", lst)

    print("The list is now sorted!")
