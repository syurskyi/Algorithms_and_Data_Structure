import sys

class PrimeTable():
    def __init__(self, bound):
        self.bound = bound
        self.primes = self.__init_primes()
        
    def __init_primes(self):
        primes = []
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(primes))
        return primes

class Problem():
    def solve(self):
        for n in [100, 1000000]:
            print("result =>", n, self.get(n))

    def get(self, bound):
        prime_table = PrimeTable(bound)
        terms = self.__generate_terms(bound)
        aux = self.__generate_aux_terms(bound)
    
        P = [0 for _ in range(bound + 1)]
        for init_term in terms:
            stack = [init_term]
            print("init stack =>", stack)
            while stack:
                top = stack[-1]
                stack.pop()
                if top[2] > bound:
                    continue
                P[top[2]] += 1
                for i in range(0, top[0]):
                    for j, d in aux[i][top[1] + 1:]:
                        next = (i, j, top[2] + d)
                        stack.append(next)
    
        rv = 0
        for q in prime_table.primes:
            if P[q] == 1:
                print("found =>", q)
                rv += q
        return rv
            
    def __generate_terms(self, bound):
        terms = []
        log2_bound = self.__get_log(bound, 2)
        log3_bound = self.__get_log(bound, 3)
        for i in range(log2_bound + 1):
            for j in range(log3_bound + 1):
                d = 2**i * 3**j
                if d > bound:
                    break
                terms.append((i, j, d))
        return terms
    
    def __generate_aux_terms(self, bound):
        terms = {}
        log2_bound = self.__get_log(bound, 2)
        log3_bound = self.__get_log(bound, 3)
        for i in range(log2_bound + 1):
            terms[i] = []
            for j in range(log3_bound + 1):
                d = 2**i * 3**j
                if d > bound:
                    break
                terms[i].append((j, d))
        return terms

    def __get_log(self, n, base):
        e = 1
        d = base
        while d * base <= n:
            e += 1
            d *= base
        return e

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())

