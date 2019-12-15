''' Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 7 (every 6 will be followed
by at least one 7). Return 0 for no numbers. '''


def sum67(nums):
    nums_sum = 0
    sum_blocked = False
    for num in nums:
        if num != 6 and not sum_blocked:
            nums_sum += num
        if num == 6:
            sum_blocked = True
        if num == 7:
            sum_blocked = False
    return nums_sum
