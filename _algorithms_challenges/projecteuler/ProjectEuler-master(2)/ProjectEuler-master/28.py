import sys

def main():
	sum = 1
	for i in range(3, 1001 + 1, 2):
		sum += 4*i*i - 6*(i-1)
	print(sum)
	
if __name__ == '__main__':
    sys.exit(main())
