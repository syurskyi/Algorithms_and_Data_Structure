import math
import sys

class OddPrimeTable():
    def get(n):
        visited_range = n // 2 + 1
        visited = [False for i in range(visited_range)]
        sqrt_n = int(math.sqrt(n)) + 1 
        for i in range(3, sqrt_n, 2):
            if visited[i // 2]:
                continue
            for j in range((i**2) // 2, visited_range, i):
                visited[j] = True
        return [i for i in range(3, n + 1, 2) if not visited[i // 2]]
        
class Problem():
    def solve(self):
        for n in [100, 500000000]:
            print(n, '=>', self.get(n))

    def get(self, n):
        odd_bound = (n + 1) // 2     
        result = [2 * i + 1 for i in range(odd_bound)]
        prime_list = OddPrimeTable.get(n)
        print('odd prime list size =>', len(prime_list))
        for prime in prime_list:
            double_prime = prime * 2
            for j in range(prime, n, double_prime):
                result[j // 2] = result[j // 2] // prime * (prime - 1)
        return sum(result)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
