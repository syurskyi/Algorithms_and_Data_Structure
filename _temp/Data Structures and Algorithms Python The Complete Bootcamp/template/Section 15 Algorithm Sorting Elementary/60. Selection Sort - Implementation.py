___ selectionSort(arr
    ___ i __ r..(l..(arr
        min_x _ i

        ___ item __ r..(i + 1, l..(arr
            __ arr[item] < arr[min_x]:
                min_x _ item

        arr[i], arr[min_x] _ arr[min_x], arr[i]


arr _ [20, 12, 10, 15, 2]
selectionSort(arr)

print(arr)