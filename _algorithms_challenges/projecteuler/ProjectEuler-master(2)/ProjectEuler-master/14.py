import sys

def collatz_length(n):
	length = 1
	while n is not 1:
		if n % 2 is 0:
			n = int(n/2)
		else:
			n = int(3*n+1)
		length += 1
	return length

def main():
	max_length_so_far = 1
	max_term_so_far = 1
	for i in range(1, 1000001):
		length = collatz_length(i)
		if length > max_length_so_far:
			max_length_so_far = length
			max_term_so_far = i
	print(max_term_so_far)

if __name__ == '__main__':
    sys.exit(main())
