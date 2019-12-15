import itertools
import sys

class Problem():
    def __init__(self):
        self.factorial = self.__init_factorial()
        self.patterns = self.__init_patterns()

    def __init_factorial(self):
        result = [1]
        d = 1
        for i in range(1, 13 + 1):
            d *= i
            result.append(d)
        return result

    def __init_patterns(self):
        result = {}
        for card_count in range(1, 4 + 1):
            result[card_count] = []
            for pattern in itertools.combinations(range(4), card_count):
                result[card_count].append([i in pattern for i in range(4)])
        return result

    def solve(self):
        count = 0
        for n in range(4, 13 + 1):
            count += self.get(n)
        print(count)

    def get(self, n):
        total_count = 0
        for distribution in itertools.product(range(13 + 1), repeat=4):
            a, b, c, d = distribution
            if a + 2 * b + 3 * c + 4 * d == n and a + b + c + d >= 4:
                permutation_count = self.factorial[a + b + c + d] // self.factorial[a] // self.factorial[b] // self.factorial[c] // self.factorial[d]
                distribution_count = 0
                
                unpacking = []
                for i in range(4):
                    unpacking += [self.patterns[(i + 1)] for j in range(distribution[i])]

                for hand in itertools.product(*unpacking):
                    badugi_count = self.__get_badugi_count(hand)
                    distribution_count += badugi_count * permutation_count

                print(distribution, '=>', distribution_count)
                total_count += distribution_count

        print(n, '=>', total_count)
        return total_count

    def __get_badugi_count(self, hand):
        suit_distribution = [[] for i in range(4)]
        curr_rank = 0
        for same_rank in hand:
            for i in range(4):
                if same_rank[i]:
                    suit_distribution[i].append(curr_rank)
            curr_rank += 1
        for i in range(4):
            if not suit_distribution[i]:
                return 0
        count = self.__binomial(13, curr_rank)
        for four_card in itertools.product(*suit_distribution):
            if len(set(four_card)) == 4:
                return count
        return 0

    def __binomial(self, n, m):
        return self.factorial[n] // self.factorial[m] // self.factorial[n - m]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
