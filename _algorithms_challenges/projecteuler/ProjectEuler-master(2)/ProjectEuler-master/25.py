import math
import sys

def main():
    upper_bound = pow(10, 999)
    curr_term = 1
    (prev_fib, curr_fib) = (0, 1)
    while curr_fib <= upper_bound: 
        (prev_fib, curr_fib) = (curr_fib, curr_fib + prev_fib)        
        curr_term += 1
    print(curr_term)

if __name__ == '__main__':
    sys.exit(main())
