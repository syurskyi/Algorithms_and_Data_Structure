import sys
from fractions import Fraction
        
class PrimeFrogProblem():        
    def __init__(self):
        self.visited = None
        
    def get_prob(self, n, croak_sequence):
        self._init_primes(n)

        prob_array = [Fraction(1, n)] * n 
        for i in range(len(croak_sequence)):
            next_prob_array = [Fraction(0)] * n
            for j in range(n):
                p = Fraction(1, 3)
                if (croak_sequence[i] == 'N') == self.visited[j]:
                    p = Fraction(2, 3)
                if j == 0:
                    next_prob_array[j+1] += prob_array[j] * p
                elif j == n - 1:
                    next_prob_array[j-1] += prob_array[j] * p
                else:
                    next_prob_array[j+1] += prob_array[j] * Fraction(1, 2) * p
                    next_prob_array[j-1] += prob_array[j] * Fraction(1, 2) * p
            prob_array = next_prob_array
        return sum(prob_array)
        
    def _init_primes(self, n):
        self.visited = [False] * (n + 1)
        self.visited[0] = self.visited[1] = True
        for i in range(2, n + 1):
            if not self.visited[i]:
                for j in range(i + i, n + 1, i):
                    self.visited[j] = True
        self.visited.pop(0)
    
def main():
    problem = PrimeFrogProblem()
    print(problem.get_prob(500, 'PPPPNNPPPNPPNPN'))
    
if __name__ == '__main__':
    sys.exit(main())
