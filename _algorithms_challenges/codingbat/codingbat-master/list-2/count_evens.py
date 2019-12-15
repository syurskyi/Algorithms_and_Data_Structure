''' Return the number of even ints in the given array. Note: the % "mod"
operator computes the remainder, e.g. 5 % 2 is 1. '''


def count_evens(nums):
    evens = 0
    for n in nums:
        if n % 2 == 0:
            evens += 1
    return evens
