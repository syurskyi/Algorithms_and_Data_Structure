import math
import sys

def C(m, n):
    return int(math.factorial(m)/(math.factorial(n)*math.factorial(m-n)))
    
def main():
    primitive_ways = 0
    ways = []
    for n in range(26):
        primitive_ways = primitive_ways * 2 + n
        ways.append(primitive_ways * C(26, n+1))
    print(max(ways))
    
if __name__ == '__main__':
    sys.exit(main())
