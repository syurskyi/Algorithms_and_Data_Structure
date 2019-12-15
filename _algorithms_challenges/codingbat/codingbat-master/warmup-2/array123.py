''' Given an array of ints, return True if the sequence of numbers 1, 2, 3
appears in the array somewhere. '''


def array123(nums):
    if len(nums) >= 3:
        for i, _ in enumerate(nums):
            if i + 2 == len(nums):
                break
            if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
                return True
    return False
