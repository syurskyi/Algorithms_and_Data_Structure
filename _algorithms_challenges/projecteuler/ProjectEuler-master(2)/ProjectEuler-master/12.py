import math
import sys

def factor_count(n):
    count = 0
    upper_bound = int(math.sqrt(n))
    for i in range(1, upper_bound + 1):
        if n % i == 0:
            count += 2
    if n == upper_bound * upper_bound:
        count -= 1        
    return count
        
def main():
    n = 0
    for i in range(1, 100000):
        n += i
        if factor_count(n) > 500:
            print(n)
            break
    
if __name__ == '__main__':
    sys.exit(main())
