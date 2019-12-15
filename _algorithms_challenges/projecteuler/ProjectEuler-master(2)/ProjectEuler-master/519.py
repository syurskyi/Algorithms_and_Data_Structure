import sys

class Problem():
    def __init__(self):
        self.mod = 10**9
        self.fountain_table = {}
        self.fountain = None
        self.primitive_fountain = None
        self.colored_fountain = None

    def solve(self):
        print(self.get(20000))

    def get(self, n):
        self.__init_fountain(n)
        self.__init_primitive_fountain(n)
        self.__init_colored_fountain(n)
        return self.colored_fountain[n]

    def __init_fountain(self, n):
        self.fountain = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            self.fountain[i] = self.__get_fountain_table(i, 1)

    def __init_primitive_fountain(self, n):
        self.primitive_fountain = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            non_primitive_fountain = 0
            for j in range(1, i):
                x = self.primitive_fountain[j]
                y = self.fountain[i - j]
                non_primitive_fountain += x * y
            self.primitive_fountain[i] = (self.fountain[i] - non_primitive_fountain) % self.mod 

    def __init_colored_fountain(self, n):
        self.colored_fountain = [0 for i in range(n + 1)]
        self.colored_fountain[0] = 1
        self.colored_fountain[1] = 3
        for i in range(2, n + 1):
            count = 2 * self.colored_fountain[i - 1] + 6 * self.primitive_fountain[i]
            for primitive_coins in range(2, i):
                x = self.primitive_fountain[primitive_coins]
                y = self.colored_fountain[i - primitive_coins]
                count += 4 * x * y
            self.colored_fountain[i] = count % self.mod

    def __get_fountain_table(self, n, k):
        if k > n:
            return 0
        if k == n:
            return 1
        if n not in self.fountain_table:
            self.fountain_table[n] = {}
        if k not in self.fountain_table[n]:
            count = 0
            for r in range(1, k + 2):
                count = (count + self.__get_fountain_table(n - k, r)) % self.mod
            self.fountain_table[n][k] = count
        return self.fountain_table[n][k]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
