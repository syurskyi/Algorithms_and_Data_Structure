___ selectionSort(arr):
    ___ i __ r.. l..(arr)):
        min_x = i

        ___ item __ r..(i + 1, len(arr)):
            __ arr[item] < arr[min_x]:
                min_x = item

        arr[i], arr[min_x] = arr[min_x], arr[i]


arr = [20, 12, 10, 15, 2]
selectionSort(arr)

print(arr)