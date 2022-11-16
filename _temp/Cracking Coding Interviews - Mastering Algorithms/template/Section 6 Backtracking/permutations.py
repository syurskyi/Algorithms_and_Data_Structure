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

___ permutation_recursive(nums, path
	__ l..(nums) __ 0:
		r_ [path]

	output _    # list

	___ i __ range(l..(nums)):
		copy_path _ copy.deepcopy(path)
		copy_path.a..(nums[i])
		permutations _ permutation_recursive(nums[:i] + nums[i + 1:], copy_path)

		output +_ permutations

	r_ output

___ permute(nums
	r_ permutation_recursive(nums,    # list)

print(permute([1, 2, 3, 4, 5, 6]))
