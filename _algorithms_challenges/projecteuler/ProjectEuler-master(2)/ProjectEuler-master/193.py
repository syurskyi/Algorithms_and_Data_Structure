import math
import sys
        
class CountingProblem():        
    def __init__(self):
        self.n = 2**50
        self.bound = 2**25
        self.sieve_visited = None
        self.mobius_functions = None
    
        self._init_mobius_functions()
        
    def _init_mobius_functions(self):
        self.mobius_functions = [1] * (self.bound + 1)
        self.mobius_functions[1] = 1
        self.sieve_visited = [False] * (self.bound + 1)
        self.sieve_visited[0] = self.sieve_visited[0] = True
        for i in range(2, self.bound + 1):
            if not self.sieve_visited[i]:
                self.mobius_functions[i] *= -1
                for j in range(i+i, self.bound + 1, i):
                    self.sieve_visited[j] = True
                    self.mobius_functions[j] *= -1    
                for j in range(i*i, self.bound + 1, i*i):
                    self.mobius_functions[j] = 0
        print('First ten Mobius function:', self.mobius_functions[1:11])
    
    def get_count(self):
        count = 0
        for d in range(1, self.bound + 1):
            count += self.mobius_functions[d] * (self.n // (d**2))
        return count
    
def main():
    problem = CountingProblem()
    print(problem.get_count())
    
if __name__ == '__main__':
    sys.exit(main())
