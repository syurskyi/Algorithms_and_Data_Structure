import math
import sys

def C(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n-k)

def main():
    billionaire_ways = 0
    for h in range(432, 1001):
        billionaire_ways += C(1000, h)
    print(billionaire_ways / 2**1000)
    
if __name__ == '__main__':
    sys.exit(main())

# Final capital = (1 + 2x)^h (1 - x)^(1000 - h) where h is the count of heads.
#
# To be a billionaire, we need (1 + 2x)^h (1 - x)^(1000 - h) >= 10^9.
# Or h >= (9 Log[10] - 1000 Log[1 - x])/(-Log[1 - x] + Log[1 + 2 x])
#
# By Wolfram Alpha website, we can solve the equation D[g(x), x] = 0
# The proportion x ~~ 0.14688392244094067657558240, and thus 
# g(x) ~~ 431.25594829396045105038827, or h = 432.
