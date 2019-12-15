import sys

class WeirdRecurrenceRelation():
    def __init__(self):
        self.cached = {}
        self.cached[1] = 1
        self.cached[3] = 3

    def get(self, n):
        if n in self.cached:
            return self.cached[n]
        if n % 2 == 0:
            results = self.get(n // 2)
            self.cached[n] = results
            return results
        elif n % 4 == 1:
            m = n // 4
            results = 2 * self.get(2*m + 1) - self.get(m)
            self.cached[n] = results
            return results
        elif n % 4 == 3:
            m = n // 4
            results = 3 * self.get(2*m + 1) - 2 * self.get(m)
            self.cached[n] = results
            return results

class WeirdRecurrenceSumRelation():
    def __init__(self):
        self.cached = {
            0: 0,
            1: 1,
            2: 2,
            3: 5,
        }
    
    def get(self, n):
        if n in self.cached:
            return self.cached[n]
        results = None
        q, r = divmod(n, 4)
        if r == 0:
            results = 6 * self.get(2*q) - 5 * self.get(q) - 3 * self.get(q - 1) - 1
        elif r == 1:
            results = 2 * self.get(2*q + 1) + 4 * self.get(2 * q) - 6 * self.get(q) - 2 * self.get(q - 1) - 1
        elif r == 2:
            results = 3 * self.get(2*q + 1) + 3 * self.get(2 * q) - 6 * self.get(q) - 2 * self.get(q - 1) - 1
        elif r == 3:
            results = 6 * self.get(2*q + 1) - 8 * self.get(q) - 1
        self.cached[n] = results
        return results

class Problem():
    def solve(self):
        relation = WeirdRecurrenceSumRelation()
        assert(relation.get(8) == 22)
        assert(relation.get(100) == 3604)
        print(relation.get(3**37) % 10**10)

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
