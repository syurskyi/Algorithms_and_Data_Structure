import sys
      
def main():
    squares = set([n*n for n in range(1, 1000)])
    for a in range(1, 1000):
        a2 = a*a
        for b in range(1, a):
            b2 = b*b
            for c in range(1, b):
                c2 = c*c
                if b2 - c2 in squares and a2 - c2 in squares and a2 - b2 in squares:
                    if (a2 + b2 + c2) % 2 == 0 and a2 > b2 - c2 and b2 > a2 - c2 and c2 > a2 - b2:
                        print('''x + y = %d''' % a2)
                        print('''x - y = %d''' % (b2 - c2))
                        print('''x + z = %d''' % b2)
                        print('''x - z = %d''' % (a2 - c2))
                        print('''y + z = %d''' % c2)
                        print('''y - z = %d''' % (a2 - b2))
                        print('''(%d, %d, %d) => %d''' % (a, b, c, (a2 + b2 + c2)/2))
        
if __name__ == '__main__':
    sys.exit(main())
