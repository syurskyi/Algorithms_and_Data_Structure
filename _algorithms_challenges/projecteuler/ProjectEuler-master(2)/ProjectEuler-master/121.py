import sys
from fractions import Fraction
    
TOTAL_TURNS = 15
    
def main():
    probability = {}
    probability[(0, 0)] = Fraction(1, 1)
    for i in range(1, TOTAL_TURNS + 1):
        for j in range(i + 1):
            probability[(j, i - j)] = Fraction(0, 1)
            if j > 0: 
                probability[(j, i - j)] += probability[(j - 1, i - j)] * Fraction(1, i + 1)
            if i - j > 0:
                probability[(j, i - j)] += probability[(j, i - j - 1)] * Fraction(i, i + 1)            
    
    total = Fraction(0, 1)
    for d in probability:
        if d[0] + d[1] == TOTAL_TURNS and d[0] > d[1]:
            print(d, probability[d])
            total += probability[d]
    print(total, int(total.denominator / total.numerator))

if __name__ == '__main__':
    sys.exit(main())
