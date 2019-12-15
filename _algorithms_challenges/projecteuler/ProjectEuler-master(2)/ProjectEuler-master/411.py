import bisect
import sys

class Problem():
    def solve(self):
        #self.benchmark()
        print(self.get())

    def benchmark(self):
        for n in [22, 123, 10000]:
            print(n, "=>", self.S(n))

    def get(self):
        result = 0
        for k in range(1, 30 + 1):
            maximum_number = self.S(k**5)
            result += maximum_number
            print(k, "=>", maximum_number)
        return result

    def S(self, n):
        station_set = set()
        for i in range(2 * n + 1):
            station = (pow(2, i, n), pow(3, i, n))
            if station in station_set:
                break
            else:
                station_set.add(station)
        sorted_station_array = sorted(list(station_set))
        y_array = [y for x, y in sorted_station_array]
        return self.get_longest_increasing_subsequence_length(y_array)

    def get_longest_increasing_subsequence_length(self, sequence):
        length = len(sequence)
        if length == 0:
            return 0
        subsequence = [sequence[0]]
        for i in range(1, length):
            n = sequence[i]
            if n >= subsequence[-1]:
                subsequence.append(n)
            else:
                subsequence[bisect.bisect_right(subsequence, n)] = n
        return len(subsequence)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
