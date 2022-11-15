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

def climb(n, i, memo):
	if n == i:
		return 1
	elif i > n:
		return 0

	if i in memo:
		return memo[i]

	num_ways = climb(n, i + 1, memo) + climb(n, i + 2, memo)
	memo[i] = num_ways

	return num_ways

def climb_stairs(n):
	return climb(n, 0, dict())


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(115))
