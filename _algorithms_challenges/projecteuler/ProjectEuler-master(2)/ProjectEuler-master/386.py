import math
import sys

class SegmentedSignatureTable():
    def __init__(self, n):
        self.n = n
        self.cut = 100
        self.cut_size = self.n // self.cut
        self.sieve_prime_list = self.__get_sieve_prime_list(n)
        self.maximum_length_cache = {}

    def get(self):
        total_count = 0
        for i in range(self.cut):
            range_begin = i * self.cut_size + 1
            range_end = (i + 1) * self.cut_size
            segmented_signature = self.__get_segmented_signature(range_begin, range_end)
            cut_count = 0
            for signature in segmented_signature:
                maximum_length = self.__get_maximum_length(signature)
                cut_count += maximum_length
            total_count += cut_count
            print('current cut =>', i, cut_count, total_count)
        return total_count

    def __get_sieve_prime_list(self, n):
        m = int(math.sqrt(n))
        return self.__get_prime_list(m)

    def __get_prime_list(self, n):
        visited = [False for _ in range(n + 1)]
        values = []
        for i in range(2, n + 1):
            if visited[i]:
                continue
            values.append(i)
            for j in range(i + i, n + 1, i):
                visited[j] = True
        return values

    def __get_segmented_signature(self, range_begin, range_end):
        range_len = range_end - range_begin + 1
        result = [[] for _ in range(range_len)]
        d_list = [range_begin + i for i in range(range_len)]
        for prime in self.sieve_prime_list:
            offset = range_begin % prime
            if offset > 0:
                offset = prime - offset
            for i in range(offset, range_len, prime):
                e = 0
                while d_list[i] % prime == 0:
                    e += 1
                    d_list[i] = d_list[i] // prime
                result[i].append(e)
        for i in range(range_len):
            if d_list[i] > 1:
                result[i].append(1)
            result[i] = tuple(sorted(result[i]))
        return result

    def __get_maximum_length(self, signature):
        if signature not in self.maximum_length_cache:
            self.maximum_length_cache[signature] = self.__get_solution_count(signature)
        return self.maximum_length_cache[signature]

    def __get_solution_count(self, signature):
        if len(signature) <= 1:
            return 1
        n = sum(signature)
        max_count_so_far = 0
        max_k_so_far = None
        for k in range(n):
            count = self.__search(signature, k)
            if count > max_count_so_far:
                max_count_so_far = count
                max_k_so_far = k
        return max_count_so_far

    def __search(self, signature, k):
        count = 0
        signature_len = len(signature)
        dfs_stack = []
        for i in range(signature[0] + 1):
            dfs_stack.append(([i], 1, i))
        while dfs_stack:
            top_vector, top_dim, top_sum = dfs_stack.pop(-1)
            if top_sum > k:
                continue
            if top_dim == signature_len:
                if top_sum == k:
                    count += 1
                continue
            for i in range(signature[top_dim] + 1):
                next_vector = top_vector + [i]
                next_dim = top_dim + 1
                next_sum = top_sum + i
                dfs_stack.append((next_vector, next_dim, next_sum))
        return count

class Problem():
    def solve(self):
        n = 10**8
        print(SegmentedSignatureTable(n).get())

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
