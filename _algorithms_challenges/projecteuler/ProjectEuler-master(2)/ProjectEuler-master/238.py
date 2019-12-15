import sys

class BlumBlumShub():
    def get(self, s0, mod):
        sequence = [s0]
        visited = set(sequence)
        s = s0
        n = 0
        while True:
            s = s**2 % mod
            n += 1
            if s in visited:
                break
            else:
                sequence.append(s)
                visited.add(s)
        return sequence

class Problem():
    def __init__(self):
        self.w = None
        self.partial_sums = None
        self.partial_sum_set = None
        self.k_range = None
        self.p_table = None
        
        self.__init_string()
        self.__init_partial_sums()
        self.__init_partial_sum_set()
        self.__init_p_table()
    
    def __init_string(self):
        blum_blum_shub = BlumBlumShub()
        sequence = blum_blum_shub.get(14025256, 20300713)
        print("blum blum shub =>", len(sequence), sequence[:10], "...")
        self.w = [0]
        for s in sequence:
            self.w.extend([int(digit) for digit in str(s)])
        print("string =>", len(self.w), self.w[:10], "...")
        
    def __init_partial_sums(self):
        curr_partial_sum = self.w[0]
        self.partial_sums = [curr_partial_sum]
        for i in range(1, len(self.w)):
            curr_partial_sum += self.w[i]
            self.partial_sums.append(curr_partial_sum)
        self.k_range = self.partial_sums[-1]
        print("partial_sums =>", len(self.partial_sums), "...", self.partial_sums[-10:])
        for i in range(1, 101):
            curr_partial_sum += self.w[i]
            self.partial_sums.append(curr_partial_sum)
        print("extending =>", len(self.partial_sums), "...", self.partial_sums[-10:])

    def __init_partial_sum_set(self):
        self.partial_sum_set = set(self.partial_sums)
        print("partial_sum_set =>", len(self.partial_sum_set))

    def __init_p_table(self):
        print("k_range =>", self.k_range)
        self.p_table = [None for _ in range(self.k_range + 1)]
        for k in range(1, self.k_range + 1):
            for z in range(1, len(self.partial_sums) + 1):
                if k + self.partial_sums[z - 1] in self.partial_sum_set:
                    self.p_table[k] = z
                    break
            if self.p_table[k] is None:
                print("It should not be here =>", k)
                raise Exception()
            if k % 1000000 == 0:
                print("Current status =>", k, self.p_table[k])
        print("Last status =>", self.k_range, self.p_table[self.k_range])

    def solve(self):
        self.benchmark()
        print(self.__get_sum(2*10**15))
    
    def benchmark(self):
        rv = self.__get_sum(1000)
        print(rv)
        assert(rv == 4742)
    
    def __get_sum(self, n):
        q, r = divmod(n, self.k_range)
        return q * sum(self.p_table[1:]) + sum(self.p_table[1:r + 1])

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
