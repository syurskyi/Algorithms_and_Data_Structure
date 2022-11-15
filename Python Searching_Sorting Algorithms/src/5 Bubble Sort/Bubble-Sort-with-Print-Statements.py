def bubble_sort(lst):

    print("========> Starting Bubble Sort\n")

    n = len(lst)

    print("Initial list:", lst)
    print("List length:", n)
    
    for i in range(n):
        print(f"\n-----> Outer Loop iteration #{i+1}\n")
            
        for j in range(0, n-1):

            print(f"-> Inner Loop iteration #{j+1}")
            print("Left element:", lst[j])
            print("Right element:", lst[j+1])
            
            if lst[j] > lst[j+1]:
                print("Not sorted:", lst[j], ">", lst[j+1])
                print("Swapping...")
                print("Old list:", lst)
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print("New list:", lst, "\n")
            # Added only for illustration purposes,
            # to add descriptive print statements for each case.
            else:
                if lst[j] < lst[j+1]:
                    print("Already sorted:", lst[j], "<", lst[j+1])
                    print("No change:", lst, "\n")
                else:
                    print("Already sorted:", lst[j], "=", lst[j+1])
                    print("No change:", lst, "\n")
