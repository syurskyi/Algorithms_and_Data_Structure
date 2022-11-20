______ copy

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

___ combos(candidates, target, path, cur_sum, candidate_index
	__ cur_sum __ target:
		r_ [path]
	____ cur_sum > target:
		r_    # list

	output _    # list

	___ i __ r..(candidate_index, l..(candidates
		cur _ candidates[i]
		copy_path _ copy.deepcopy(path)
		copy_path.a..(cur)

		combinations _ combos(candidates, target, copy_path, cur_sum + cur, i)

		output +_ combinations

	r_ output

___ combo_sum(candidates, target
	r_ combos(candidates, target,    # list, 0, 0)

print(combo_sum([2,3,6,7], 7))


print(combo_sum([2,3,5], 8))





