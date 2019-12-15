from math import factorial
import sys

def C(n, m):
    return factorial(n) // factorial(m) // factorial(n - m)

def main():
    sample_space_size = factorial(100)
    event_size = C(25, 3) * sum([(-1)**i * C(22, i) * factorial(97-i) for i in range(23)])
    print(event_size / sample_space_size)
    
if __name__ == '__main__':
    sys.exit(main())
