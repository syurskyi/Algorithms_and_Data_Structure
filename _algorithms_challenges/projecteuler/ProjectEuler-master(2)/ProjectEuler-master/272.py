import bisect
import sys

class GoodPrimeTable():
    def build(self, sieve_range):
        factor = 3**2 * 7 * 13 * 19
        shrinked_sieve_range = sieve_range // factor
        result = []
        visited = [False for _ in range(shrinked_sieve_range)]
        for i in range(2, shrinked_sieve_range):
            if visited[i] is True:
                continue
            if i % 3 == 1:
                result.append(i)
            for j in range(i + i, shrinked_sieve_range, i):
                visited[j] = True
        return result

class Problem():
    def __init__(self):
        self.sieve_range = 10**11
        self.table = GoodPrimeTable().build(self.sieve_range)

    def solve(self):
        print('Count:', self.get_sum_excluding_9() + self.get_sum_including_9())

    def get_sum_excluding_9(self):
        sum = 0
        n = len(self.table)
        performance_counter = 0
        for i in range(n):
            p_i = self.table[i]
            for j in range(i + 1, n):
                p_j = self.table[j]
                p_ij = p_i * p_j
                if p_ij > self.sieve_range:
                    break
                for k in range(j + 1, n):
                    p_k = self.table[k]
                    p_ijk = p_ij * p_k
                    if p_ijk > self.sieve_range:
                        break
                    for h in range(k + 1, n):
                        p_h = self.table[h]
                        p_ijkh = p_ijk * p_h
                        if p_ijkh > self.sieve_range:
                            break
                        for t in range(h + 1, n):
                            p_t = self.table[t]
                            p_all = p_ijkh * p_t
                            if p_all > self.sieve_range:
                                break
                            max_bound = self.sieve_range // p_all
                            including = [p_i, p_j, p_k, p_h, p_t]
                            excluding = [9]
                            good_factor_sum = self.get_good_factor_sum(max_bound, including, excluding)
                            sum += good_factor_sum * p_all

                            performance_counter += 1
                            if performance_counter % 100000 == 0:
                                print('Excluding 9:', max_bound, including, good_factor_sum, sum)
        print(sum)
        return sum

    def get_sum_including_9(self):
        sum = 0
        n = len(self.table)
        performance_counter = 0
        for i in range(n):
            p_i = self.table[i]
            p_i9 = p_i * 9
            if p_i9 > self.sieve_range:
                break
            for j in range(i + 1, n):
                p_j = self.table[j]
                p_ij = p_i9 * p_j
                if p_ij > self.sieve_range:
                    break
                for k in range(j + 1, n):
                    p_k = self.table[k]
                    p_ijk = p_ij * p_k
                    if p_ijk > self.sieve_range:
                        break
                    for h in range(k + 1, n):
                        p_h = self.table[h]
                        p_all = p_ijk * p_h
                        if p_all > self.sieve_range:
                            break
                        max_bound = self.sieve_range // p_all
                        including = [p_i, p_j, p_k, p_h]
                        good_factor_sum = self.get_good_factor_sum(max_bound, including)
                        sum += good_factor_sum * p_all
        
                        performance_counter += 1
                        if performance_counter % 100000 == 0:
                            print('Including 9:', max_bound, including, good_factor_sum, sum)
        print(sum)
        return sum
            
    def get_good_factor_sum(self, max_bound, including, excluding=set()):
        good_set = set([_ for _ in range(1, max_bound + 1)])
        bad_numbers = set(self.table[:bisect.bisect_right(self.table, max_bound)])
        bad_numbers -= set(including)
        bad_numbers |= set(excluding)
        for i in bad_numbers:
            good_set -= set([_ for _ in range(i, max_bound + 1, i)])
        return sum(good_set)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
