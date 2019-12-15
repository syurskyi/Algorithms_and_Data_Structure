import sys

def main():
    # Reuse the fact that 2520 is the smallest number that can be divided 
    # by each of the numbers from 1 to 10 without any remainder.
    print(2520 * 11 * 13 * 2 * 17 * 19)
    
if __name__ == '__main__':
    sys.exit(main())
