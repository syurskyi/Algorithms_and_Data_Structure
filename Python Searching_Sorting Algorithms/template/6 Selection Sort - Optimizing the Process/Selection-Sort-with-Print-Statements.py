def selection_sort(lst):
    
	print("\n===========> Starting Selection Sort <===========\n")
	
	for i in range(len(lst)):

		print(f"\n=========> Outer Loop iteration #{i+1}\n")

		if i != len(lst) - 1:
			print("List:", lst)
			print("Sorted portion:", lst[:i])
			print("Unsorted portion:", lst[i:])
			print("The unsorted portion starts at index:", i)
		else:
			print("The list is now sorted!")
			print(lst)
			break
		 
		min_index = i

		for curr_index in range(i+1, len(lst)):
			
			print(f"\n--> Inner Loop iteration")

			print("Current element:", lst[curr_index])
			print("Min element so far:", lst[min_index])

			print("Is the current element smaller than the min element?", "Yes" if lst[min_index] > lst[curr_index] else "No")
			
			if lst[min_index] > lst[curr_index]:
				min_index = curr_index
				print(lst[curr_index], "is now the new min element. It is located at index:", min_index)
			else:
				print("No need to change the min element")

		print("\n-> Out of inner loop")
		print("Previous list:", lst)
		print("\nSwapping the first element in the unsorted portion:", lst[i])
		print("With the min element found:", lst[min_index])
		lst[i], lst[min_index] = lst[min_index], lst[i]
		print("New list:", lst)
