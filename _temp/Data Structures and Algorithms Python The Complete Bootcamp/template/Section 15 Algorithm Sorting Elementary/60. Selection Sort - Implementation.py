___ selectionSort(arr
    ___ i __ range(len(arr)):
        min_x _ i

        ___ item __ range(i + 1, len(arr)):
            __ arr[item] < arr[min_x]:
                min_x _ item

        arr[i], arr[min_x] _ arr[min_x], arr[i]


arr _ [20, 12, 10, 15, 2]
selectionSort(arr)

print(arr)