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

___ mark_island(grid, i, j
	__ i < 0 or i >_ l..(grid) or j < 0 or j >_ l..(grid[0]) or grid[i][j] __ 0:
		r_

	grid[i][j] _ 0

	dirs _ [[1, 0], [-1, 0], [0, 1], [0, -1]]

	___ d __ dirs:
		mark_island(grid, i + d[0], j + d[1])

___ num_islands(grid
	__ l..(grid) __ 0 or l..(grid[0]) __ 0:
		r_ 0

	count _ 0

	___ i __ range(l..(grid)):
		___ j __ range(l..(grid[0])):
			__ grid[i][j] __ 1:
				mark_island(grid, i, j)
				count +_ 1

	r_ count


grid1 _ [
	[1,1,1,1,0],
	[1,1,0,1,0],
	[1,1,0,0,0],
	[0,0,0,0,0],
]

grid2 _ [
	[1,1,0,0,0],
	[1,1,0,0,0],
	[0,0,1,0,0],
	[0,0,0,1,1],
]

print(num_islands(grid1))
print(num_islands(grid2))


