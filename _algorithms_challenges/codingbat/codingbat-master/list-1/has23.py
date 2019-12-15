''' Given an int array length 2, return True if it contains a 2 or a 3. '''


def has23(nums):
    has_23 = False
    for num in nums:
        if num in [2, 3]:
            has_23 = True
    return has_23
