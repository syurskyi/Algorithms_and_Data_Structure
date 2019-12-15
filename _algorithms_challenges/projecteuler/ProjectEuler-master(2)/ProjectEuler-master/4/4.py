import sys

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def main():
    P = []
    for i in range(100, 1000): 
        for j in range(100, 1000):
            if is_palindrome(i*j):
                P += [int(i*j)]
    print(sorted(P)[-1])
    
if __name__ == '__main__':
    sys.exit(main())
