# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right



# Example 2:

# Input: m = 7, n = 3
# Output: 28

# [
# 	[1, 1, 1],
# 	[1, 2, 3],
# ]

def unique_paths_rec(m, n, i, j, memo):
	if m - 1 == i and n - 1 == j:
		return 1
	elif i >= m or j >= n:
		return 0

	key = str(i) + "," + str(j)

	if key in memo:
		return memo[key]

	num_paths = unique_paths_rec(m, n, i + 1, j, memo) + unique_paths_rec(m, n, i, j + 1, memo)
	memo[key] = num_paths

	return num_paths

def unique_paths(m, n):
	return unique_paths_rec(m, n, 0, 0, dict())

print(unique_paths(3, 2))
print(unique_paths(7, 3))

print(unique_paths(15, 15))
