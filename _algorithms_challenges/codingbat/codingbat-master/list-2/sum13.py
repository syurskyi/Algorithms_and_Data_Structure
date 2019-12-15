''' Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that
come immediately after a 13 also do not count. '''


def sum13(nums):
    nums_sum = 0
    after_13_index = -1
    for i, num in enumerate(nums):
        if num != 13 and i != after_13_index:
            nums_sum += num
        if num == 13 and i != (len(nums) - 1):
            after_13_index = i + 1
    return nums_sum
