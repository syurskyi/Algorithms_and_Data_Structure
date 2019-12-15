import sys

def main():
    count = 0
    (numerator, denominator) = (1, 1)
    for i in range(1, 1001):
        (numerator, denominator) = (numerator + denominator * 2, denominator + numerator)
        if len(str(numerator)) > len(str(denominator)):
            count += 1
    print(count)
            
if __name__ == '__main__':
    sys.exit(main())
