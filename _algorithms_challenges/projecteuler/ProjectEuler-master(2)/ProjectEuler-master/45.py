import sys

def main():
    T = set([int(n*(n+1)/2) for n in range(1, 100000)])
    P = set([int(n*(3*n-1)/2) for n in range(1, 100000)])
    H = set([int(n*(2*n-1)) for n in range(1, 100000)])
    print(T.intersection(P).intersection(H))

if __name__ == '__main__':
    sys.exit(main())
