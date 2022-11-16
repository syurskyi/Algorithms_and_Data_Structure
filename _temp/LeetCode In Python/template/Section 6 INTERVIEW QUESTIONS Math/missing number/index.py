c_ Solution:
    ___ missingNumber nums: List[int]) -> int:
        currentSum _ sum(nums)
        n _ len(nums)
        intendedSum _ n*(n+1)/2

        r_ int(intendedSum-currentSum)
