import sys

class MonotonousQueue():
    def __init__(self, array, k):
        self.array = array
        self.k = k

    def get_sum(self):
        result = 0
        queue = []
        for i in range(self.k):
            queue.append((self.array[i], i+1))
        queue.sort(reverse=True)
        result += queue[0][0]
        N = len(self.array)
        for i in range(self.k, N):
            d = self.array[i]
            curr_index = i+1
            while True:
                if not queue:
                    queue.append((d, curr_index))
                    break
                last = queue[-1][0]
                if last < d:
                    queue.pop()
                else:
                    queue.append((d, curr_index))
                    break
            top_d, top_index = None, None
            while True:
                top_d, top_index = queue[0]
                if curr_index - top_index >= self.k:
                    queue.pop(0)
                else:
                    break
            result += top_d
            if i % 1000000 == 0:
                print("=>", (d, i+1), result)
        return result

class Problem():
    def solve(self):
        print(self.get(1000, 10))
        print(self.get(100000000, 100000))
    
    def get(self, u, k):
        divisor_counts = self.get_divisor_counts(u)
        queue = MonotonousQueue(divisor_counts, k)
        return queue.get_sum()
    
    def get_divisor_counts(self, u):
        rv = [1 for _ in range(u + 1)]
        for i in range(u + 1):
            rv[i] = 1
        for i in range(2, u + 1):
            if i % 1000000 == 0:
                print("i =>", i)
            if rv[i] != 1:
                continue
            for j in range(i, u + 1, i):
                d = j
                e = 0
                while d % i == 0:
                    d //= i
                    e += 1
                rv[j] *= (e + 1)
        print("Completed divisor counts")
        return rv[1:]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
