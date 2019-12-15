import sys

class Problem():
    def __init__(self):
        self.problem_range = 10**11
        self.good_primes = []
        self.range_counting = None

        self._init_primes(self.problem_range // (5**3 * 13**2) + 1)
        self._init_range_counting()
        
    def solve(self):
        n = len(self.good_primes)
        count = 0
        for i in range(n):
            p = self.good_primes[i]
            if p**2 > self.problem_range:
                break
            for j in range(i+1, n):
                q = self.good_primes[j]
                if p**2 * q**2 > self.problem_range:
                    break
                count += self._get_count(p**10 * q**2)
                count += self._get_count(p**2 * q**10)
                count += self._get_count(p**7 * q**3)
                count += self._get_count(p**3 * q**7)
                for k in range(j+1, n):
                    r = self.good_primes[k]
                    good_product = p**3 * q**2 * r
                    if good_product > self.problem_range:
                        break
                    count += self._get_count(good_product)
                    count += self._get_count(p**3 * q * r**2)
                    count += self._get_count(p**2 * q**3 * r)
                    count += self._get_count(p**2 * q * r**3)
                    count += self._get_count(p * q**3 * r**2)
                    count += self._get_count(p * q**2 * r**3)
        print(count)
        
    def _init_primes(self, sieve_range):
        visited = [False] * sieve_range
        visited[0] = visited[1] = True
        for i in range(2, sieve_range):
            if visited[i]:
                continue
            if i % 4 == 1:
                self.good_primes.append(i)
            for j in range(i+i, sieve_range, i):
                visited[j] = True
        print('Prime of form (4k+1) count:', len(self.good_primes))
    
    def _init_range_counting(self):
        count_range = self.problem_range // (5**3 * 13**2 * 17) + 1 
        visited = [False] * count_range
        visited[0] = True
        for p in self.good_primes:
            for q in range(p, count_range, p):
                visited[q] = True
        self.range_counting = [0] * count_range
        for i in range(1, count_range):
            self.range_counting[i] = self.range_counting[i-1]
            if visited[i] is False:
                self.range_counting[i] += i
        print('Range counting:', len(self.range_counting))
        
    def _get_count(self, good_product):
        return self.range_counting[self.problem_range // good_product] * good_product
        
def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
