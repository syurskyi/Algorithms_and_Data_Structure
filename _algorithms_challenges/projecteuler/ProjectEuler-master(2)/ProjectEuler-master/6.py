import sys

def main():
    N = 100
    print(int((N*(N+1)/2)*(N*(N+1)/2) - (N*(N+1)*(2*N+1))/6))
    
if __name__ == '__main__':
    sys.exit(main())
