from heapq import heappush, heappop
import sys

class Problem():
    def solve(self):
        for n in [6, 10**9]:
            print(n, '=>', self.get(n))

    def get(self, n):
        h = []
        heappush(h, (1, 1))
        heappush(h, (4, 1))
        i = 0
        while i < n - 2:
            cost, frequency = heappop(h)
            # Merge
            next_cost, next_frequency = heappop(h)
            if next_cost != cost:
                heappush(h, (next_cost, next_frequency))
            else:
                frequency += next_frequency

            # Generate next state (cost, frequency) for next prefix codes
            if i + frequency < n - 2: 
                heappush(h, (cost + 1, frequency))
                heappush(h, (cost + 4, frequency))
                i += frequency
            else:
                heappush(h, (cost, frequency - n + 2 + i))
                heappush(h, (cost + 1, n - 2 - i))
                heappush(h, (cost + 4, n - 2 - i))
                break

        total_cost = 0
        total_frequency = 0
        for cost, frequency in h:
            total_cost += cost * frequency
            total_frequency += frequency
        assert(total_frequency == n)
        return total_cost

if __name__ == '__main__':
    sys.exit(Problem().solve())
