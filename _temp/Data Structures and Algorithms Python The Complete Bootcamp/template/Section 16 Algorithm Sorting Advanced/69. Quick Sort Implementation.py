___ quickSort(my_array
    qshelper(my_array, 0, l..(my_array) - 1)
    r_ my_array


___ qshelper(my_array, start, end
    __ start >_ end:
        r_

    pivot _ start
    left _ start + 1
    right _ end

    _____ right >_ left:

        __ my_array[left] > my_array[pivot] ___ my_array[right] < my_array[pivot]:
            my_array[left], my_array[right] _ my_array[right], my_array[left]

        __ my_array[left] <_ my_array[pivot]:
            left +_ 1

        __ my_array[right] >_ my_array[pivot]:
            right -_ 1

    my_array[pivot], my_array[right] _ my_array[right], my_array[pivot]

    qshelper(my_array, start, right - 1)
    qshelper(my_array, right + 1, end)