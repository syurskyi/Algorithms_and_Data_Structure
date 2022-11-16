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

___ unique_paths(m, n
	arr _ [[0 ___ j __ range(m)] ___ i __ range(n)]

	___ i __ range(n
		___ j __ range(m
			__ i == 0 or j == 0:
				arr[i][j] _ 1
			____
				arr[i][j] _ arr[i - 1][j] + arr[i][j - 1]

	r_ arr[n - 1][m - 1]

print(unique_paths(3, 2))
print(unique_paths(7, 3))
