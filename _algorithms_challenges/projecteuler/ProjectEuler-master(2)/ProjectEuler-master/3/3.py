import sys

def main():
    primes = set(range(2, 780000))
    for i in range(2, 780000): 
        primes -= set(range(2*i, 780000, i))
    
    d = 600851475143
    factor = []
    for p in primes:
        while (d % p == 0):
            d /= p
            factor += [p]
    if d != 1:
        factor += [int(d)]
        
    print(factor[-1])
    
if __name__ == '__main__':
    sys.exit(main())
