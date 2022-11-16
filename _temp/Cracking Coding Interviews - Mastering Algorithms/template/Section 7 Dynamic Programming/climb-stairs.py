# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:


# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

___ climb(n, i, memo
	__ n == i:
		r_ 1
	elif i > n:
		r_ 0

	__ i __ memo:
		r_ memo[i]

	num_ways _ climb(n, i + 1, memo) + climb(n, i + 2, memo)
	memo[i] _ num_ways

	r_ num_ways

___ climb_stairs(n
	r_ climb(n, 0, dict())


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(115))
