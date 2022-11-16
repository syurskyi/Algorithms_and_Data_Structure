c_ Solution:
    ___ twoSum nums, target
        store _ {}

        ___ i __ range(l..(nums)):
            __ nums[i] __ store:
                r_ [store[nums[i]], i]
            ____
                store[target-nums[i]] _ i


## Example Execution ##
obj _ Solution()
result _ obj.twoSum([2,7,11,15], 9)
print(result)