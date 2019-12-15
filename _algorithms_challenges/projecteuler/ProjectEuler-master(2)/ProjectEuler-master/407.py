import sys

SIEVE_RANGE = 10**7 + 1
primes = []

def sieve():
    visited = [False] * SIEVE_RANGE
    for i in range(2, SIEVE_RANGE):
        if visited[i] is False:
            primes.append(i)
            for j in range(i+i, SIEVE_RANGE, i):
                visited[j] = True
    print('''sieve completed, the last prime is %d''' % primes[-1])

def get_max_idempotent_root(n):
    d = n
    m = 1
    roots = [0, 1]
    for prime in primes:
        if prime * prime > d:
            break
        if d % prime != 0:
            continue
        power_prime = 1
        while d % prime == 0:
            power_prime *= prime
            d = int(d/prime)
        curr_roots = []
        for a in [0, 1]:
            for b in roots:
                curr_roots.append(solve_equations(a, power_prime, b, m))
        roots = curr_roots
        m *= power_prime
    if d > 1:
        curr_roots = []
        for a in [0, 1]:
            for b in roots:
                curr_roots.append(solve_equations(a, d, b, m))
        roots = curr_roots
    return max(roots)
    
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
    sum = 0
    # M(1) = 0
    for i in range(2, SIEVE_RANGE):
        max_root = get_max_idempotent_root(i)
        sum += max_root
        if i % 10000 == 0:
            print('''Current number: %d => %d''' % (i, max_root))
    print(sum)
    
if __name__ == '__main__':
    sys.exit(main())
