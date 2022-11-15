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

def unique_paths(m, n):
	arr = [[0 for j in range(m)] for i in range(n)]

	for i in range(n):
		for j in range(m):
			if i == 0 or j == 0:
				arr[i][j] = 1
			else:
				arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

	return arr[n - 1][m - 1]

print(unique_paths(3, 2))
print(unique_paths(7, 3))
