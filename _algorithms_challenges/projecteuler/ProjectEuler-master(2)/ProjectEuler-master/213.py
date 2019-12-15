import itertools
import sys
from fractions import Fraction
        
class FleaCircusProblem():        
    def __init__(self, size):
        self.n = size
        self.flea_prob = [[None for _ in range(self.n)] for _ in range(self.n)]
        for x, y in itertools.product(range(self.n), repeat=2):
            self.flea_prob[x][y] = [[Fraction(0) for i in range(self.n)] for j in range(self.n)]
            self.flea_prob[x][y][x][y] = Fraction(1)
    
    def ring_bell(self, times):
        for i in range(times):
            print('Ring times:', i+1)
            self._ring_bell_once()
        unoccupied_prob = [[1.0 for i in range(self.n)] for j in range(self.n)]
        for x, y in itertools.product(range(self.n), repeat=2):
            for i, j in itertools.product(range(self.n), repeat=2):
                unoccupied_prob[i][j] *= float(1 - self.flea_prob[x][y][i][j])     
        expected_number = 0.0
        for i, j in itertools.product(range(self.n), repeat=2):
            expected_number += unoccupied_prob[i][j]
        print(expected_number)
        
    def _ring_bell_once(self):
        for x, y in itertools.product(range(self.n), repeat=2):
            self.flea_prob[x][y] = self._jump(self.flea_prob[x][y])
    
    def _jump(self, curr_prob):
        next_prob = [[Fraction(0) for i in range(self.n)] for j in range(self.n)]
        for i, j in itertools.product(range(self.n), repeat=2):
            if (i, j) == (0, 0):
                next_prob[i][j+1] += Fraction(1, 2) * curr_prob[i][j]
                next_prob[i+1][j] += Fraction(1, 2) * curr_prob[i][j]
            elif (i, j) == (0, self.n - 1):
                next_prob[i][j-1] += Fraction(1, 2) * curr_prob[i][j]
                next_prob[i+1][j] += Fraction(1, 2) * curr_prob[i][j]
            elif (i, j) == (self.n - 1, 0):
                next_prob[i-1][j] += Fraction(1, 2) * curr_prob[i][j]
                next_prob[i][j+1] += Fraction(1, 2) * curr_prob[i][j]
            elif (i, j) == (self.n - 1, self.n - 1):
                next_prob[i][j-1] += Fraction(1, 2) * curr_prob[i][j]
                next_prob[i-1][j] += Fraction(1, 2) * curr_prob[i][j]
            elif i == 0:
                next_prob[i][j-1] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i][j+1] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i+1][j] += Fraction(1, 3) * curr_prob[i][j]
            elif i == self.n - 1:
                next_prob[i][j-1] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i][j+1] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i-1][j] += Fraction(1, 3) * curr_prob[i][j]
            elif j == 0:
                next_prob[i-1][j] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i+1][j] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i][j+1] += Fraction(1, 3) * curr_prob[i][j]
            elif j == self.n - 1:
                next_prob[i-1][j] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i+1][j] += Fraction(1, 3) * curr_prob[i][j]
                next_prob[i][j-1] += Fraction(1, 3) * curr_prob[i][j]
            else:
                next_prob[i-1][j] += Fraction(1, 4) * curr_prob[i][j]
                next_prob[i+1][j] += Fraction(1, 4) * curr_prob[i][j]
                next_prob[i][j-1] += Fraction(1, 4) * curr_prob[i][j]
                next_prob[i][j+1] += Fraction(1, 4) * curr_prob[i][j]
        return next_prob
        
def main():
    problem = FleaCircusProblem(30)
    problem.ring_bell(50)
    
if __name__ == '__main__':
    sys.exit(main())
