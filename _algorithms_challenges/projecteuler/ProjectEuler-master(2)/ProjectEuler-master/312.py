import sys

class ExtendedGCD():
    def solve(a, b):
        x, y = 0, 1
        last_x, last_y = 1, 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, last_x = last_x - q * x, x
            y, last_y = last_y - q * y, y
        return last_x, last_y

# Solve x = a_i (mod n_i) where n_i are coprime.
class ChineseRemainderTheorem():
    def solve(a_list, n_list):
        a = a_list[0]
        m = n_list[0]
        for i in range(1, len(n_list)):
            n = n_list[i]
            b = a_list[i]
            q = m * n
            x, y = ExtendedGCD.solve(m, n)
            root = (a + (b - a) * x * m) % q
            a, m = root, q
        return a

# Solve ax = 1 (mod m).
class ModInverse():
    def solve(a, m):
        x, y = ExtendedGCD.solve(a, m)
        return x % m

class Problem():
    def solve(self):
        x1 = self.get_c(10000, 12 * 13**4) 
        x2 = pow(3, x1 - 2, 13**5)
        x3 = ((x2 - 3) * ModInverse.solve(2, 13**5)) % 13**5
        x4 = ChineseRemainderTheorem.solve([3, x3], [12, 13**5])
        x5 = (8 * pow(12, x4, 13**6)) % 13**6 # C(C(10000)) (mod 13^6) = 2792886
        x6 = ChineseRemainderTheorem.solve([0, x5], [12, 13**6]) # C(C(10000)) (mod 12 * 13^6) = 31753740
        x7 = pow(3, x6 - 2, 13**7)
        x8 = ((x7 - 3) * ModInverse.solve(2, 13**7)) % 13**7
        x9 = ChineseRemainderTheorem.solve([3, x8], [12, 13**7])
        result = (8 * pow(12, x9, 13**8)) % 13**8 # C(C(C(10000))) (mod 13^8) = 324681947
        print(result)

    def get_c(self, n, mod):
        return (8 * pow(12, (3**(n - 2) - 3) // 2, mod)) % mod

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
