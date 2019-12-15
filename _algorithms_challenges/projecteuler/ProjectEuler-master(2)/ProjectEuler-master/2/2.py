import sys

def main():
    sum = 0
    (prev_fib, curr_fib) = (0, 1)
    while curr_fib < 4000000: 
        if curr_fib % 2 == 0:
            sum += curr_fib
        (prev_fib, curr_fib) = (curr_fib, curr_fib + prev_fib)        
    print(sum)

if __name__ == '__main__':
    sys.exit(main())
