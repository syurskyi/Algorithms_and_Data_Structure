___ mergeSort(my_array
    __ l..(my_array) __ 1:
        r_ my_array

    middle _ l..(my_array) // 2
    left _ my_array[:middle]
    right _ my_array[middle:]

    left_result _ mergeSort(left)
    right_result _ mergeSort(right)

    r_ merge(left_result, right_result)


___ merge(left_result, right_result
    result _ [N..] * (l..(left_result) + l..(right_result))
    i _ j _ k _ 0

    _____ i < l..(left_result) ___ j < l..(right_result
        __ left_result[i] <_ right_result[j]:
            result[k] _ left_result[i]
            i +_ 1
        ____
            result[k] _ right_result[j]
            j +_ 1
        k +_ 1

    _____ i < l..(left_result
        result[k] _ left_result[i]
        i +_ 1
        k +_ 1

    _____ j < l..(right_result
        result[k] _ right_result[j]
        j +_ 1
        k +_ 1

    r_ result


numbers _ [4, 5, 6, 1, 3, 7, 2]
print(mergeSort(numbers))