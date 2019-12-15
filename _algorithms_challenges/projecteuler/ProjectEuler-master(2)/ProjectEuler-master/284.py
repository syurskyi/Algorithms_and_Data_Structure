import sys

class AutomorphicNumberGenerator():
    def __init__(self):
        self.base = None
        self.digit_rep = '0123456789abcdefghijklmnopqrstuvwxyz'
        
    def generate(self, base, max_digit_count):
        assert(base in [10, 14])
        self.base = base
        
        all_digit_sums = 1 # Trivial cases: 0^0 = 0 and 1^2 = 1.
        for n in range(1, max_digit_count + 1):
            if n % 100 == 0:
                print('Current num of digit (every 100):', n)
            for num in self._generate_n_digit(n):        
                digit_sum = self._get_digit_sum(num)
                all_digit_sums += digit_sum
        print('Digit sum:', self._to_literal(all_digit_sums))
        
    def _generate_n_digit(self, n):
        rv = set()
        a, b = (self.base // 2)**n, 2**n
        x, y = self._extended_gcd(a, b)
        lower_bound = self.base**(n-1)
        k = a*(x % b)
        if k >= lower_bound:
            rv.add(k)
        k = a*((-x) % b) + 1
        if k >= lower_bound:
            rv.add(k)
        return rv
    
    def _extended_gcd(self, a, b):
        (x, y) = (0, 1)
        (last_x, last_y) = (1, 0)
        while b != 0:
            (q, r) = divmod(a, b);
            (a, b) = (b, r)
            (x, last_x) = (last_x - q * x, x)
            (y, last_y) = (last_y - q * y, y)
        return (last_x, last_y)
    
    def _get_digit_sum(self, num):
        rv = 0
        q = num
        while q:
            q, r = divmod(q, self.base)
            rv += r
        return rv
    
    def _to_literal(self, num):
        rv_backtrace = ''
        q = num
        while q:
            q, r = divmod(q, self.base)
            rv_backtrace += self.digit_rep[r]
        return rv_backtrace[::-1]
    
def main():
    g = AutomorphicNumberGenerator()
    g.generate(14, 10000)
    
if __name__ == '__main__':
    sys.exit(main())
