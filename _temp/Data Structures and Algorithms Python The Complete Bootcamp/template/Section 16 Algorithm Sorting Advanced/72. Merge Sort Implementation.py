___ mergeSort(my_array
    __ len(my_array) == 1:
        r_ my_array

    middle _ len(my_array) // 2
    left _ my_array[:middle]
    right _ my_array[middle:]

    left_result _ mergeSort(left)
    right_result _ mergeSort(right)

    r_ merge(left_result, right_result)


___ merge(left_result, right_result
    result _ [N..] * (len(left_result) + len(right_result))
    i _ j _ k _ 0

    _____ i < len(left_result) and j < len(right_result
        __ left_result[i] <_ right_result[j]:
            result[k] _ left_result[i]
            i +_ 1
        ____
            result[k] _ right_result[j]
            j +_ 1
        k +_ 1

    _____ i < len(left_result
        result[k] _ left_result[i]
        i +_ 1
        k +_ 1

    _____ j < len(right_result
        result[k] _ right_result[j]
        j +_ 1
        k +_ 1

    r_ result


numbers _ [4, 5, 6, 1, 3, 7, 2]
print(mergeSort(numbers))