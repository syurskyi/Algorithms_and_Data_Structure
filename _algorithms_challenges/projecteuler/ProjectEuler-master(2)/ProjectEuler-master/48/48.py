import sys

def main():
    z = 10**10
    print(sum([pow(i, i, z) for i in range(1, 1001)]) % z)
    
if __name__ == '__main__':
    sys.exit(main())
