def merge_sort(lst):

    print("\n======> Calling merge_sort()")

    print("List:", lst)
    print("List length:", len(lst))
    
    if len(lst) == 0 or len(lst) == 1:
        print("The list is empty or it only contains one item")
        print("Returning list:", lst)
        return lst
    else:
        middle_index = len(lst)//2
        print("Middle index:", middle_index)
        print("Left half:", lst[:middle_index])
        print("Right half:", lst[middle_index:])

        print("Calling merge_sort() for the left half:", lst[:middle_index])
        left = merge_sort(lst[:middle_index])
        print("Calling merge_sort() for the right half:", lst[middle_index:])
        right = merge_sort(lst[middle_index:])

        # Small adjustments to the original implementation
        # for the print statements
        print("Merging the two halves...")
        final_list = merge(left, right)
        
        print("\nBack to merge_sort()")
        print("Resulting merged list:", final_list)

        return final_list


def merge(left_half, right_half):

    print("\n---> Inside merge()")

    print("Merging...")
    print("Left half", left_half)
    print("Right half", right_half)

    if not left_half or not right_half:
        print("One of the lists is empty")
        print("Returning", left_half or right_half)
        return left_half or right_half
    
    result = []
    i, j = 0, 0

    print("\n-> While loop")
    while True:
        print("i =", i)
        print("j =", j)

        print(f"\nIs the element left_half[i] ({left_half[i]}) < the element right_half[j] ({right_half[j]})")
        if left_half[i] < right_half[j]:
            print("Yes,it is!")
            print(f"Append the element left_half[i] ({left_half[i]}) to the list 'result'")
            print("List 'result' before:", result)
            result.append(left_half[i])
            print("List 'result' after:", result)
            i += 1
            print("We've assigned one element of the left half")
            print("Incrementing the value of i to:", i)

        else:
            print("No, it isn't!")
            print(f"Appending right_half[j] ({right_half[j]}) to the list 'result'")
            print("List 'result' before:", result)
            result.append(right_half[j])
            print("List 'result' after:", result)
            j += 1
            print("We've assigned one element of the right half")
            print("Incrementing the value of j to:", j)
            
        print("\nHave we reached the end of either one of the lists?", "Yes" if i == len(left_half) or j == len(right_half) else "No")
        if i == len(left_half) or j == len(right_half):
            print("We reached the end of", "the left half" if i == len(left_half) else "the right half")
            print("Extending the list 'result' with the remaining item(s):", left_half[i:] or right_half[j:])
            result.extend(left_half[i:] or right_half[j:])
            break
        else:
            print("Let's continue the while loop")

    print("Returning the list 'result':", result)
    return result
