import sys

def main():
    for a in range(0, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c > b and a*a + b*b == c*c:
                print(a*b*c)
    
if __name__ == '__main__':
    sys.exit(main())
