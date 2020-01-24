import copy

# Given a set of candidate numbers (candidates)
# (without duplicates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]



# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

def combos(candidates, target, path, cur_sum, candidate_index):
	if cur_sum == target:
		return [path]
	elif cur_sum > target:
		return []

	output = []

	for i in range(candidate_index, len(candidates)):
		cur = candidates[i]
		copy_path = copy.deepcopy(path)
		copy_path.append(cur)

		combinations = combos(candidates, target, copy_path, cur_sum + cur, i)

		output += combinations

	return output

def combo_sum(candidates, target):
	return combos(candidates, target, [], 0, 0)

print(combo_sum([2,3,6,7], 7))


print(combo_sum([2,3,5], 8))





