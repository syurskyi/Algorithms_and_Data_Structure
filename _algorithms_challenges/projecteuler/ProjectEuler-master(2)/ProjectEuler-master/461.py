import math
import sys

class Problem():
    def solve(self):
        print(self.g(200))
        print(self.g(10000))

    def g(self, n):
        sub_g = self.get_sub_g(n)
        begin_pos = 0
        end_pos = len(sub_g) - 1
        best_delta_so_far = math.pi
        best_index_so_far = [0, 0, 0, 0]
        while begin_pos <= end_pos:
            total_sum =sub_g[begin_pos][1] + sub_g[end_pos][1]
            delta = abs(total_sum - math.pi)
            if delta < best_delta_so_far:
                best_delta_so_far = delta
                best_index_so_far = self.unhash(sub_g[begin_pos][0]) + self.unhash(sub_g[end_pos][0])
                print(best_delta_so_far, best_index_so_far)
            if total_sum > math.pi:
                end_pos -= 1
            else:
                begin_pos += 1
        results = 0
        for i in best_index_so_far:
            results += i**2
        return results

    def get_sub_g(self, n):
        sub_g = {}
        max_k = self.get_max_k(n)
        for i in range(max_k):
            for j in range(i, max_k):
                sub_sum = self.f(n, i) + self.f(n, j)
                if sub_sum < math.pi:
                    sub_g[self.hash(i, j)] = sub_sum
                else:
                    break
        return sorted(sub_g.items(), key=lambda x: x[1])

    def hash(self, i, j):
        return '%d-%d' % (i, j)
    
    def unhash(self, hashed_string):
        return list(map(int, hashed_string.split('-')))
    
    def f(self, n, k):
        return math.exp(k / n) - 1

    def get_max_k(self, n):
        k = int(n * math.log(math.pi + 1)) + 1
        assert(self.f(n, k) > math.pi)
        assert(self.f(n, k-1) < math.pi)
        return k

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())