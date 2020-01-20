# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.


# Example 1
# nums = [2, 7, 11, 15], target = 9
# return [0, 1]

# 7 => 0

# Example 2
# nums = [2, 7, 11, 15, 4, 23, 19, 5], target = 19
# return [3, 4]

# Brute force O(n^2)
# O(n) + O(n)

def twosum(nums, target):
	dic = {}

	for i in range(len(nums)):
		if nums[i] in dic.keys():
			return [dic[nums[i]], i]
		else:
			dic[target - nums[i]] = i

	return []

print(twosum([2, 7, 11, 15], 9))
print(twosum([2, 7, 11, 15, 4, 23, 19, 5], 19))
