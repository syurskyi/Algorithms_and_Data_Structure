from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # j indicates the no. of non-zero elements that we have,
        # currently it's at index 0, which mean that we have 0 non-zero
        j = 0
        for num in nums:
            if(num != 0):
                # if current element is not zero, set
                # the element at j to it and increment j
                nums[j] = num
                j += 1
        # after loop ends, set all elements from
        # position j to end of array to zero
        for x in range(j, len(nums)):
            nums[x] = 0

s = Solution()
print(s.moveZeroes([0, 2, 0, 1, 4]))
