import bisect
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
        #print('Prime count:', len(primes))
        return primes

class Problem():
    def solve(self):
        for n in [4, 500500]:
            print(n, '=>', self.get(n))

    def get(self, n):
        primes = self.__get_primes(n)
        rep = self.__get_rep(primes, n)
        return self.__get_value(rep, 500500507)

    def __get_primes(self, n):
        prime_counting_function = [4, 25, 168, 1229, 9592, 78498, 664579]
        e = bisect.bisect_left(prime_counting_function, n)
        return PrimeTable().get(10**(e + 1))

    def __get_rep(self, primes, n):
        rep = [[2], [], [], [], []]
        x = 1
        for i in range(1, n):
            p = primes[x]
            is_promoted = False
            for e in range(4, -1, -1):
                if not rep[e]:
                    continue
                top = rep[e][0]
                y = top**(2**(e + 1))
                if p > y:
                    rep[e + 1].append(top)
                    rep[e].pop(0)
                    is_promoted = True
                    break
            if not is_promoted:
                rep[0].append(p)
                x += 1
        return rep

    def __get_value(self, rep, mod):
        result = 1
        for e in range(len(rep)):
            for p in rep[e]:
                result = (result * p**(2**(e + 1) - 1)) % mod
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
