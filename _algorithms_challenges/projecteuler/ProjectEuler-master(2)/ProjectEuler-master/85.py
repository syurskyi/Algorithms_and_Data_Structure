import sys

def main():
	# Number of rectangles = C(n,2) * C(m,2) where grid is (n-1) by (m-1).
	# Use the fact that: C(2001,2) = 2001000 and C(2,2) = 1.
	# If we cannot find the nearest solution, output 2000.
	nearest_so_far = 1999999
	nearest_grid_area_so_far = 1
	for n in range(1, 2001): 
		for m in range(n, 2001):
			num_rectangles = int(n*(n-1)/2) * int(m*(m-1)/2)
			nearest = abs(num_rectangles - 2000000)
			if nearest < nearest_so_far:
				nearest_so_far = nearest
				nearest_grid_area_so_far = (n-1) * (m-1)
	print(nearest_grid_area_so_far)
				
if __name__ == '__main__':
    sys.exit(main())
