import bisect
import sys

class IntegerPartition():
    def __init__(self, max_n):
        self.values = self.__init_values(max_n)

    def get(self, n):
        return self.values[n]

    def __init_values(self, max_n):
        result = {}
        for n in range(1, max_n + 1):
            result[n] = list(self.__generate(n))
        return result

    def __generate(self, n):
        a = [0 for i in range(n + 1)]
        k = 1
        a[1] = n
        while k != 0:
            x = a[k - 1] + 1
            y = a[k] - 1
            k -= 1
            while x <= y:
                a[k] = x
                y -= x
                k += 1
            a[k] = x + y
            yield a[:k + 1]

class Factorial():
    def __init__(self, n):
        self.values = [1]
        for i in range(1, n + 1):
            self.values.append(self.values[-1] * i)
  
    def get(self, n):
        return self.values[n]

class AlphabeticalOrder():
    def __init__(self, phrase, max_length):
        self.alphabet_count = None
        self.alphabet_order = None
        self.max_length = max_length
        self.partition = IntegerPartition(max_length)
        self.factorial = Factorial(max_length)
        self.ways_with_prefix_cache = {'' : 0}

        self.__init_alphabets(phrase)

    def __init_alphabets(self, phrase):
        self.alphabet_count = {}
        for alphabet in phrase:
            if alphabet not in self.alphabet_count:
                self.alphabet_count[alphabet] = 0
            self.alphabet_count[alphabet] += 1
        self.alphabet_order = sorted(list(self.alphabet_count))

    def P(self, word):
        total_ways = len(word)
        for prefix in self.__get_prefix_list(word):
            ways = 1 + self.__get_ways_with_prefix(prefix)
            total_ways += ways
        return total_ways

    def W(self, order):
        word = ''
        while True:
            prev_word = None
            for alphabet in self.alphabet_order:
                curr_word = word + alphabet
                if not self.__is_valid_word(curr_word):
                    continue
                curr_word_order = self.P(curr_word)                
                if curr_word_order == order:
                    return curr_word
                elif curr_word_order > order:
                    word = prev_word
                    break
                else:
                    prev_word = curr_word
        
    def __get_prefix_list(self, word):
        for i in range(len(word)):
            pos = bisect.bisect_left(self.alphabet_order, word[i])
            good_alphabet_list = self.alphabet_order[:pos]
            for alphabet in good_alphabet_list:
                prefix = word[:i] + alphabet
                if self.__is_valid_word(prefix):
                    yield prefix

    def __is_valid_word(self, word):
        word_count = {}
        for alphabet in word:
            if alphabet not in word_count:
                word_count[alphabet] = 0
            word_count[alphabet] += 1
        for alphabet in word_count:
            if alphabet not in self.alphabet_count:
                return False
            if self.alphabet_count[alphabet] < word_count[alphabet]:
                return False
        return True

    def __get_ways_with_prefix(self, prefix):
        if prefix not in self.ways_with_prefix_cache:
            total_ways = 0
            left_alphabet_count = self.__get_left_alphabet_count(prefix)
            sorted_count_list = self.__get_sorted_count_list(left_alphabet_count)
            for i in range(1, self.max_length - len(prefix) + 1):
                for count_list in self.partition.get(i):
                    ways = self.__get_permutation_count(count_list)
                    count_list = count_list[::-1]
                    right_pos = len(sorted_count_list)
                    for j in range(len(count_list)):
                        left_pos = bisect.bisect_left(sorted_count_list, count_list[j])
                        alphabet_ways = right_pos - left_pos
                        ways *= alphabet_ways
                        right_pos -= 1
                    repeated_ways = self.__get_repeated_ways(count_list)
                    total_ways += ways // repeated_ways
            self.ways_with_prefix_cache[prefix] = total_ways
        return self.ways_with_prefix_cache[prefix]

    def __get_left_alphabet_count(self, word):
        result = dict(self.alphabet_count)
        for alphabet in word:
            result[alphabet] -= 1
        return result

    def __get_sorted_count_list(self, alphabet_count):
        count_list = []
        for alphabet in alphabet_count:
            count = alphabet_count[alphabet]
            if count > 0:
                count_list.append(count)
        sorted_count_list = sorted(count_list)
        return sorted_count_list

    def __get_permutation_count(self, partition):
        denominator = 1
        partition_of_integer = 0
        for i in partition:
            denominator *= self.factorial.get(i)
            partition_of_integer += i
        numerator = self.factorial.get(partition_of_integer)
        return numerator // denominator

    def __get_repeated_ways(self, partition):
        repeated_map = {}
        for i in partition:
            if i not in repeated_map:
                repeated_map[i] = 0
            repeated_map[i] += 1
        result = 1
        for i in repeated_map:
            result *= self.factorial.get(repeated_map[i])
        return result

class Problem():
    def __init__(self):
        self.alphabetical_order = AlphabeticalOrder('thereisasyetinsufficientdataforameaningfulanswer', 15)

    def solve(self):
        #self.benchmark()
        self.get()

    def benchmark(self):
        assert(self.W(10) == 'aaaaaacdee')
        assert(self.W(115246685191495243) == 'euler')
        assert(self.P('a') == 1)
        assert(self.P('aa') == 2)
        assert(self.P('aaa') == 3)
        assert(self.P('aaaa') == 4)
        assert(self.P('aaaaa') == 5)
        assert(self.P('aaaaaa') == 6)
        assert(self.P('aaaaaac') == 7)
        assert(self.P('aaaaaacd') == 8)
        assert(self.P('aaaaaacde') == 9)
        assert(self.P('aaaaaacdee') == 10)
        assert(self.P('aaaaaacdeee') == 11)
        assert(self.P('aaaaaacdeeee') == 12)
        assert(self.P('aaaaaacdeeeee') == 13)
        assert(self.P('aaaaaacdeeeeee') == 14)
        assert(self.P('aaaaaacdeeeeeef') == 15)
        assert(self.P('aaaaaacdeeeeeeg') == 16)
        assert(self.P('aaaaaacdeeeeeeh') == 17)
        assert(self.P('aaaaaacdeeeeeey') == 28)
        assert(self.P('aaaaaacdeeeeef') == 29)
        assert(self.P('aaaaaacdeeeeefe') == 30)
        assert(self.P('euleoywuttttsss') == 115246685191495242)
        assert(self.P('euler') == 115246685191495243)
        assert(self.P('eulera') == 115246685191495244)
        assert(self.P('ywuuttttssssrrr') == 525069350231428029)

    def get(self):
        p = self.P('legionary') \
            + self.P('calorimeters') \
            - self.P('annihilate') \
            + self.P('orchestrated') \
            - self.P('fluttering')
        w = self.W(p)
        print(p, "=>", w)

    def P(self, word):
        return self.alphabetical_order.P(word)

    def W(self, order):
        return self.alphabetical_order.W(order)

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())