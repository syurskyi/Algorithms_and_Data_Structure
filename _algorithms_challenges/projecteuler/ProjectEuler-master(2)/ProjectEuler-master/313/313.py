import sys

class PrimeTable():
    def get(self, bound):
        primes = []
        visited = [False] * (bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, bound + 1):
            if not visited[i]:
                primes.append(i)
            for j in range(i + i, bound + 1, i):
                visited[j] = True
        print('Prime count:', len(primes))
        return primes

class Problem():
    def solve(self):
        for n in [100, 10**6]:
            print(n, self.get_count(n))
    
    def get_count(self, prime_range):
        count = 0
        for p in PrimeTable().get(prime_range):
            if p == 2:
                continue
            x = (p**2 - 3) // 2
            count += (x // 3 - x // 4) * 2
        return count

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

