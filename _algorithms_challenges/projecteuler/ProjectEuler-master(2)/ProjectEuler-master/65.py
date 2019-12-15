import sys

def main():
    (numerator, denominator) = (1, 0)
    for i in range(99, 0, -1):
        if (i%3 == 2): 
            k = (int(i/3) + 1) * 2 
        else:
            k = 1
        (numerator, denominator) = (denominator + numerator * k, numerator)
    (numerator, denominator) = (numerator * 2 + denominator, numerator)
    print(sum(int(digit) for digit in str(numerator)))

if __name__ == '__main__':
    sys.exit(main())
