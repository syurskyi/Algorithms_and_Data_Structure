import sys

def main():
    primes = set(range(2, 2000000))
    for i in range(2, 2000000): 
        primes -= set(range(2*i, 2000000, i))    
    print(sum(primes))
    
if __name__ == '__main__':
    sys.exit(main())
