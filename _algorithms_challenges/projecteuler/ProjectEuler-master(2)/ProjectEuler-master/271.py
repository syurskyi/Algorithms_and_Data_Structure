import sys

primes = []
cubic_roots = {}

def sieve():
    visited = [False] * 45
    for i in range(2, 45):
        if visited[i] is False:
            primes.append(i)
            set_cubic_roots(i)
            for j in range(i+i, 45, i):
                visited[j] = True

def get_sum():
    sol = cubic_roots[2]
    m = 2
    for prime in primes:
        if prime is 2:
            continue
        temp = []
        for i in sol:
            for j in cubic_roots[prime]:
                temp.append(solve_equations(i, m, j, prime))
        sol = temp
        m *= prime
    return sum(sol) - 1
    
def set_cubic_roots(prime):
    for i in range(1, prime):
        if i**3 % prime is 1:
            if prime not in cubic_roots:
                cubic_roots.update({prime : [i]})
            else:
                cubic_roots.update({prime : cubic_roots[prime] + [i]})

def solve_equations(a, m, b, n):
    q = m*n
    (x, y) = extended_gcd(m, n)
    root = a + (b - a) * x * m
    return ((root % q) + q) % q
                
def extended_gcd(a, b):
    (x, y) = (0, 1)
    (last_x, last_y) = (1, 0)
    while b != 0:
        (q, r) = divmod(a, b);
        (a, b) = (b, r)
        (x, last_x) = (last_x - q * x, x)
        (y, last_y) = (last_y - q * y, y)
    return (last_x, last_y)
                
def main():
    sieve()
    print(get_sum())
        
if __name__ == '__main__':
    sys.exit(main())
