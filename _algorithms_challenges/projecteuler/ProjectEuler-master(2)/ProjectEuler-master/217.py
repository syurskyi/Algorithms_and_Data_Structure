import sys

class Problem():
    def solve(self):
        results = 0
        for n in range(1, 47 + 1):
            results += self.get(n)
        print(results % (3**15))

    def get(self, n):
        if n == 1:
            return 45
        head = self.get_head(n)
        tail = self.get_tail(n)

        results = 0
        q, r = divmod(n, 2)
        for digit_sum in head:
            if r == 0:
                results += head[digit_sum][1] * tail[digit_sum][0] * 10**q + \
                        tail[digit_sum][1] * head[digit_sum][0]
            else:
                results += (head[digit_sum][1] * tail[digit_sum][0] * 10**(q + 1) \
                                + tail[digit_sum][1] * head[digit_sum][0]) * 10 \
                        + 45 * 10**q * head[digit_sum][0] * tail[digit_sum][0]
        return results

    def get_head(self, n):
        head = {}
        for digit in range(1, 10):
            head[digit] = [1, digit]
        for i in range(n // 2 - 1):
            curr_head = {}
            for digit in range(0, 10):
                for old_digit_sum in head:
                    curr_digit_sum = old_digit_sum + digit
                    if curr_digit_sum not in curr_head:
                        curr_head[curr_digit_sum] = [0, 0]
                    curr_head[curr_digit_sum][0] += head[old_digit_sum][0]
                    curr_head[curr_digit_sum][1] += head[old_digit_sum][1] * 10 + digit * head[old_digit_sum][0]
            head = curr_head
        return head

    def get_tail(self, n):
        tail = {}
        for digit in range(0, 10):
            tail[digit] = [1, digit]
        for i in range(n // 2 - 1):
            curr_tail = {}
            for digit in range(0, 10):
                for old_digit_sum in tail:
                    curr_digit_sum = old_digit_sum + digit
                    if curr_digit_sum not in curr_tail:
                        curr_tail[curr_digit_sum] = [0, 0]
                    curr_tail[curr_digit_sum][0] += tail[old_digit_sum][0]
                    curr_tail[curr_digit_sum][1] += tail[old_digit_sum][1] * 10 + digit * tail[old_digit_sum][0]
            tail = curr_tail
        return tail

def main():
    problem = Problem()
    problem.solve()
    
if __name__ == '__main__':
    sys.exit(main())
