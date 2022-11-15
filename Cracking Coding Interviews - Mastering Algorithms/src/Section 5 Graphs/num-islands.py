# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1


# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

def mark_island(grid, i, j):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
		return

	grid[i][j] = 0

	dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

	for d in dirs:
		mark_island(grid, i + d[0], j + d[1])

def num_islands(grid):
	if len(grid) == 0 or len(grid[0]) == 0:
		return 0

	count = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				mark_island(grid, i, j)
				count += 1

	return count


grid1 = [
	[1,1,1,1,0],
	[1,1,0,1,0],
	[1,1,0,0,0],
	[0,0,0,0,0],
]

grid2 = [
	[1,1,0,0,0],
	[1,1,0,0,0],
	[0,0,1,0,0],
	[0,0,0,1,1],
]

print(num_islands(grid1))
print(num_islands(grid2))


