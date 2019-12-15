import sys

def main():
	perimeter_count = [0] * 1001
	for a in range(1, 501):
		for b in range(a, 501):
			for c in range(b, 1001-a-b):
				if a**2 + b**2 == c**2:
					perimeter_count[a+b+c] += 1
	max_count_so_far = 0
	max_perimeter_so_far = 0
	for i in range(1, 1001):
		if perimeter_count[i] > max_count_so_far:
			max_perimeter_so_far = i
			max_count_so_far = perimeter_count[i]
	print(max_perimeter_so_far)
	
if __name__ == '__main__':
    sys.exit(main())
