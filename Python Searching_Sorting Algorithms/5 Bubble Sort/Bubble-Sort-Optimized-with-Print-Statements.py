def bubble_sort(lst):

    print("========> Starting Bubble Sort\n")

    n = len(lst)

    print("Initial list:", lst)
    print("List length:", n)
    
    for i in range(n):
        print(f"\n-----> Outer Loop iteration #{i+1}\n")
        
        swapped = False
            
        for j in range(0, n-i-1):

            print(f"-> Inner Loop iteration #{j+1}")
            
            print("Left element:", lst[j])
            print("Right element:", lst[j+1])
            if lst[j] > lst[j+1]:
                print("Not sorted:", lst[j], ">", lst[j+1])
                print("Swapping...")
                print("Old list:", lst)
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print("New list:", lst, "\n")
                swapped = True
            # Added only for illustration purposes,
            # to add descriptive print statements for each case.
            else:
                if lst[j] < lst[j+1]:
                    print("Already sorted:", lst[j], "<", lst[j+1])
                    print("No change:", lst, "\n")
                else:
                    print("Already sorted:", lst[j], "=", lst[j+1])
                    print("No change:", lst, "\n")
                
        if not swapped:
            print("There was no need to swap! The list is now sorted")
            print(lst)
            break
