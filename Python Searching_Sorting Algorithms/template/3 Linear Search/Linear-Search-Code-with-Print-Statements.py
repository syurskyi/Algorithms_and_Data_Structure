def linear_search(main_list, item):
	print("Starting Linear Search Algorithm")
	for i in range(len(main_list)):
		print(f"============ Iteration #{i} ============")
		print("Current list item:", main_list[i])
		print("Item searched:", item)
		print("Is the current item equal to the item searched?", main_list[i] == item)
		if main_list[i] == item:
			print(f"Item found! at index {i}")
			return i
		print("This is not the item")
	print("The item is not in the list")
	return -1


[["Jack", "456-342", 56], ("Emily", "231-523", 15), "Nora", [True, False]]

([("Rose", 45, 5.6), [1, 2, 3]], ("a", "b", "c"), "Puppy", [4, 7, 8])


<var>[<start>:<end>:<step>]



["Kelly", "Gino", "Katherine", "James", "Lulu"]



def linear_search(main_list, item):
	print("Starting Linear Search Algorithm")
	for i in range(len(main_list)):
		print(f"============ Iteration #{i} ============")
		print("Current list item id:", main_list[i])
		print("Target id:", item)
		print("Is the current item id equal to the id searched?", main_list[i] == item)
		if main_list[i].id_num == item:
			print(f"ID found! at index {i}")
			return i
		print("This is not the id")
	print("The object is not in the list")
	return -1


