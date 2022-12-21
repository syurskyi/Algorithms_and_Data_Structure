___ mergeSort(my_array):
    __ len(my_array) __ 1:
        r_ my_array

    middle = len(my_array) // 2
    left = my_array[:middle]
    right = my_array[middle:]

    left_result = mergeSort(left)
    right_result = mergeSort(right)

    r_ merge(left_result, right_result)


___ merge(left_result, right_result):
    result = [N..] *  l..(left_result) + len(right_result))
    i = j = k = 0

    ______ i < len(left_result) and j < len(right_result):
        __ left_result[i] <= right_result[j]:
            result[k] = left_result[i]
            i += 1
        ____
            result[k] = right_result[j]
            j += 1
        k += 1

    ______ i < len(left_result):
        result[k] = left_result[i]
        i += 1
        k += 1

    ______ j < len(right_result):
        result[k] = right_result[j]
        j += 1
        k += 1

    r_ result


numbers = [4, 5, 6, 1, 3, 7, 2]
print(mergeSort(numbers))