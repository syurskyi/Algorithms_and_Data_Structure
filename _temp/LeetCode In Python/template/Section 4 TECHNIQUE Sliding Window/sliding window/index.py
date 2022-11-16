___ maxSum(arr, windowSize
    arraySize _ l..(arr)
    # n must be greater than k
    __ arraySize <_ windowSize:
        print("Invalid operation")
        r_ -1

    # Compute sum of first window of size k
    window_sum _ sum([arr[i] ___ i __ range(windowSize)])
    max_sum _ window_sum
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    ___ i __ range(arraySize-windowSize
        window_sum _ window_sum - arr[i] + arr[i + windowSize]
        max_sum _ max(window_sum, max_sum)

    r_ max_sum


arr _ [1, 2, 100, -1, 5]
# maximum sum should be 104 => 100 + -1 + 5
answer _ maxSum(arr, 3)
print(answer)
