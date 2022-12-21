___ quickSort(my_array):
    qshelper(my_array, 0, len(my_array) - 1)
    r_ my_array


___ qshelper(my_array, start, end):
    __ start >= end:
        r_

    pivot = start
    left = start + 1
    right = end

    ______ right >= left:

        __ my_array[left] > my_array[pivot] and my_array[right] < my_array[pivot]:
            my_array[left], my_array[right] = my_array[right], my_array[left]

        __ my_array[left] <= my_array[pivot]:
            left += 1

        __ my_array[right] >= my_array[pivot]:
            right -= 1

    my_array[pivot], my_array[right] = my_array[right], my_array[pivot]

    qshelper(my_array, start, right - 1)
    qshelper(my_array, right + 1, end)