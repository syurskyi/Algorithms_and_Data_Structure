import itertools
import sys
        
class PrimeConnectionProblem():
    def __init__(self):
        self.primes = []
        self.prime_literals = set()
        self.graph = {}
        self.relative_prime_literals = set()
        
    def get_non_relative_sum(self):
        self._init_prime_table(10**7)
        self._build_graph()
        rv = 0
        for p in self.primes:
            if not self._is_relative(p):
                rv += int(p)
            else:
                self.relative_prime_literals.add(str(p))
        return rv
        
    def _init_prime_table(self, bound):
        visited = [False for _ in range(bound + 1)]
        visited[0], visited[1] = True, True
        for i in range(2, bound + 1):
            if visited[i] is False:
                self.primes.append(i)
                self.prime_literals.add(str(i))
                for j in range(i + i, bound + 1, i):
                    visited[j] = True
        print('Prime count =>', len(self.prime_literals))
    
    def _build_graph(self):
        for p in self.prime_literals:
            self.graph[p] = set()
        for p in self.prime_literals:
            # Have the same length and differ in exactly one digit
            for digit in range(1, 10):
                q = str(digit) + p[1:]
                if q in self.prime_literals and p != q:
                    self.graph[p].add(q)
                    self.graph[q].add(p)
            for diff_place in range(1, len(p)):
                for digit in range(0, 10):
                    q = p[:diff_place] + str(digit) + p[diff_place+1:]
                    if q in self.prime_literals and p != q:
                        self.graph[p].add(q)
                        self.graph[q].add(p)
            # Add one digit to the left
            for digit in range(1, 10):
                q = str(digit) + p
                if q in self.prime_literals:
                    self.graph[p].add(q)
                    self.graph[q].add(p)

    def _is_relative(self, prime):
        dfs_stack = [str(prime)]
        visited = set()
        while dfs_stack:
            top = dfs_stack[-1]
            dfs_stack.pop(-1)
            if top == '2':
                return True
            if top in self.relative_prime_literals:
                return True
            if top in visited:
                continue
            visited.add(top)
            for q in self.graph[top]:
                if int(q) < prime:
                    dfs_stack.append(q)
        return False
    
def main():
    problem = PrimeConnectionProblem()
    print(problem.get_non_relative_sum())
    
if __name__ == '__main__':
    sys.exit(main())
