''' Given an array of ints, return True if 6 appears as either the first or
last element in the array. The array will be length 1 or more. '''


def first_last6(nums):
    if 6 in [nums[0], nums[-1]]:
        return True
    return False
