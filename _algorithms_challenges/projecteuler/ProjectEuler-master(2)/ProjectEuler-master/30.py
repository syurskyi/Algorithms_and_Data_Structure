import sys

def digit_power(number, power):
	sum = 0
	while number > 0:
		digit = int(number % 10)
		sum += digit**power
		number = int(number / 10)
	return sum

def main():
	S = []
	# 1000000 > 9^5 + 9^5 + 9^5 + 9^5 + 9^5 + 9^5 + 9^5
	for i in range(2, 1000000):
		if i == digit_power(i, 5):
			S.append(i)
	print(sum(S))
			
if __name__ == '__main__':
    sys.exit(main())
