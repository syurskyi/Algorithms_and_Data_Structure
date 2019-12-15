from typing import List


def list_to_decimal(nums: List[int]) -> int:
    """Accept a list of positive integers in the range(0, 10)
       and return a integer where each int of the given list represents
       decimal place values from first element to last.  E.g
        [1,7,5] => 175
        [0,3,1,2] => 312
        Place values are 10**n where n represents the digit position
        Eg to calculate 1345, we have 5 1's, 4 10's, 3 100's and 1 1000's
        1,     3  ,  4  , 5
        1000's, 100's, 10's, 1's
    """
    if not all(isinstance(num, int) for num in nums):
        raise TypeError

    if not all(num in range(0, 10) for num in nums):
        raise ValueError

    return int(''.join(map(str, nums)))