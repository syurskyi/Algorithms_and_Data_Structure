import copy
# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

def permutation_recursive(nums, path):
	if len(nums) == 0:
		return [path]

	output = []

	for i in range(len(nums)):
		copy_path = copy.deepcopy(path)
		copy_path.append(nums[i])
		permutations = permutation_recursive(nums[:i] + nums[i + 1:], copy_path)

		output += permutations

	return output

def permute(nums):
	return permutation_recursive(nums, [])

print(permute([1, 2, 3, 4, 5, 6]))
