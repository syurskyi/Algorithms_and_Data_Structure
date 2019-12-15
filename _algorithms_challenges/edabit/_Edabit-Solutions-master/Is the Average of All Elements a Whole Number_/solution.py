def is_avg_whole(arr):
    index = 0
    total = 0
    while index < len(arr):
        total = total + arr[index]
        index = index + 1
    return total % len(arr) == 0
