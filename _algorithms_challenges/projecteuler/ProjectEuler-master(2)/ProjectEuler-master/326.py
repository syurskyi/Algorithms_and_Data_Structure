import sys

class Problem():
    def solve(self):
        for n, m in [(10, 10), (10**4, 10**3), (10**12, 10**6)]:
            print(n, m, '=>', self.get(n, m))

    def get(self, n, m):
        cycle_partial_sums = self.__get_cycle_partial_sums(m)
        cycle_frequency_map = self.__get_frequency_map(cycle_partial_sums, m)

        frequency_map = [0 for _ in range(m)]
        frequency_map[0] = 1
        q, r = divmod(n, 6 * m)
        for i in range(r):
            frequency_map[cycle_partial_sums[i]] += 1
        for i in range(m):
            frequency_map[i] += (cycle_frequency_map[i] * q)
        
        result = 0
        for i in frequency_map:
            x = i * (i - 1) // 2
            result += x
        return result

    def __get_cycle_partial_sums(self, m):
        cycle = [0, 1]
        partial_sum = 0
        for i in range(2, 6 * m):
            partial_sum = partial_sum + (i - 1) * cycle[i - 1]
            cycle.append(partial_sum % i)
        cycle = cycle[1:] + cycle[:1]
        cycle_partial_sums = [cycle[0]]
        for i in range(1, 6 * m):
            x = (cycle_partial_sums[-1] + cycle[i]) % m
            cycle_partial_sums.append(x)
        return cycle_partial_sums
        
    def __get_frequency_map(self, array, m):
        result = [0 for _ in range(m)]
        for i in array:
            result[i % m] += 1
        return result

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
