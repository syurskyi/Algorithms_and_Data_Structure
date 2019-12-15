"""Helper functions for Project Euler problems"""

import itertools
from functools import reduce
from math import factorial, gcd, sqrt
from pathlib import Path


def get_path(*args) -> Path:
    """Construct a path from components, relative to the project root."""

    # A module's __file__ attribute contains an absolute path by default
    return Path(__file__).parents[1].joinpath(*args)


def sum_digits(num: int) -> int:
    """Sum the digits of a number."""
    s = 0
    while num:
        s, num = s + num % 10, num // 10
    return s


def is_prime(n):
    """Determine whether a number is prime using trial division"""

    if n < 2:
        return False
    if n in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}:
        return True
    if not (n % 2 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and
            n % 17 and n % 19 and n % 23 and n % 29):
        return False

    # all primes are of the form c#k + i for i < c# and i coprime to c#
    # let c = 6, c# = 2*3*5 = 30

    for divisor in range(30, int(sqrt(n))+1, 30):
        if not (n % (divisor + 1) and n % (divisor + 7) and
                n % (divisor + 11) and n % (divisor + 13) and
                n % (divisor + 17) and n % (divisor + 19) and
                n % (divisor + 23) and n % (divisor + 29)):
            return False
    return True


def prime_sieve(n):
    """
    Return all prime numbers <= n.
    Implements The Sieve of Eratosthenes
    """

    if n <= 1:
        return []

    bound = (n-1) // 2  # last index of the sieve
    sieve = [True]*(bound+1)

    for i in range(1, int(sqrt(n)//2)+1):
        if sieve[i]:  # 2*i+1 is a prime, mark multiples
            for j in range(2*i*(i+1), bound+1, 2*i+1):
                sieve[j] = False
    primes = [2]
    for i in range(1, bound+1):
        if sieve[i]:
            primes.append(2*i+1)
    return primes


def prime_sieve_lazy():
    """
    The Sieve of Eratosthenes (lazy version)
    http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
    """
    yield 2
    n = 3
    composites = {}

    while True:
        factors = composites.pop(n, None)
        if factors is None:
            yield n
            composites[n*n] = [n]
        else:
            for prime in factors:
                composites.setdefault(n + prime*2, []).append(prime)
        n += 2


def prime_factors(n, primes=None):
    """
    Return prime factors of an integer.
    'primes' should be None or a list of primes up to sqrt(n)
    """

    if primes is None:
        primes = prime_sieve(int(sqrt(n)))

    factors = []

    for prime in primes:
        if prime*prime > n:
            break

        if n % prime == 0:
            n //= prime
            exponent = 1
            while n % prime == 0:
                n //= prime
                exponent += 1
            factors.append((prime, exponent))
    if n > 1:
        factors.append((n, 1))

    return factors


def num_of_divisors(num: int, primes: list=None) -> int:
    """
    Returns the number of divisors of an integer.
    `primes`, if provided, should be a list of primes at least up to sqrt(n).
    """

    return reduce(lambda x, y: x*(y[1]+1), prime_factors(num, primes), 1)


def sum_of_divisors(n, primes=None):
    if n == 1:
        return 1
    # http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
    return reduce(lambda x,y: x * (y[0]**(y[1]+1)-1)//(y[0]-1), prime_factors(n, primes), 1)


def sum_of_proper_divisors(n, primes=None):
    """Return the sum of the proper divisors of a number"""
    return sum_of_divisors(n, primes) - n


def pdsums_sieve(limit):
    """Return a list of proper divisors sums for numbers under limit"""
    dsums = [1]*limit

    for i in range(2, int(sqrt(limit))):
        dsums[i*i] += i

        for j in range(i+1, -(-limit // i)):  # ceil
            dsums[i*j] += i + j
    dsums[0] = dsums[1] = 0
    return dsums


def is_palindrome(number, base=10):
    """Checks if a number is palindromic in the given base."""
    forward = number
    reverse = 0
    while number:
        reverse = reverse * base + number % base
        number //= base
    return forward == reverse


def is_pandigital(n):
    """
    Check if a number is (zeroless) pandigital in base 10, e.g. "923456781".
    No *strict* checking for redundant digits is made.
    """
    # the number must be divisible by 9
    if n % 9:
        return False

    flags = 0

    while n:
        flags |= (1 << n % 10)
        n //= 10

    return flags == 0b1111111110


def is_permutation(a, b):
    """Check if an integer is a permutation of another"""
    if (a - b) % 9:  # the difference must be a multiple of 9.
        return False
    return sorted(str(a)) == sorted(str(b))


# functions for calculating polygonal numbers
def nth_triangle(n):
    return n*(n+1)//2


def nth_square(n):
    return n*n


def nth_pentagonal(n):
    return n*(3*n - 1)//2


def nth_hexagonal(n):
    return n*(2*n-1)


def nth_heptagonal(n):
    return n*(5*n-3)//2


def nth_octagonal(n):
    return n*(3*n - 2)


def isqrt(num):
    """
    Calculate the integer square root of a positive integer using
    Newton's (Babylonian) method.
    """
    x = 1 << -(-num.bit_length() >> 1)  # ceil
    y = (x + num//x) >> 1
    while x > y:
        x = y
        y = (x + num//x) >> 1
    return x


def triangular_numbers():
    """Generate triangular numbers"""
    return itertools.accumulate(itertools.count(1))


def pentagonal_numbers():
    """Generate pentagonal numbers"""
    return itertools.accumulate(itertools.count(1, 3))


def hexagonal_numbers():
    """Generate hexagonal numbers"""
    return itertools.accumulate(itertools.count(1, 4))


def is_triangular_number(num):
    """
    Check if a number is triangular.
    An integer x is triangular if and only if 8x + 1 is a square.
    """
    return is_square(8*num + 1)


def is_pentagonal(n):
    """
    Test whether an integer n is a pentagonal number.
    """
    root = is_square(24*n+1)
    return root and root % 6 == 5


def pythagorean_triplets(p):
    """
    Return Pythagorean triplets with a+b+c=p using the formula a+b+c = 2*m*(m+n)*d
    p is always even
    http://projecteuler.net/overview=009
    """
    p >>= 1

    for m in range(2, int(sqrt(p)+1)):
        if p % m == 0:
            pm = p // m
            while not pm & 1:  # reduce the search space by removing all factors 2
                pm >>= 1
            k = m + 2 if m & 1 else m + 1

            while k < 2*m and k <= pm:
                if pm % k == 0 and gcd(k, m) == 1:
                    d = p//(k*m)
                    n = k - m
                    a = d*(m*m - n*n)
                    b = 2*d*m*n
                    c = d*(m*m + n*n)
                    yield (a, b, c)
                k += 2


def n_choose_k(n, k):
    """Returns the number of k-combinations of a set of n elements"""
    return factorial(n) // (factorial(k) * factorial(n - k))


def sqrt_fraction_expansion(num):
    """
    Returns continued fraction expansion of a square root, e.g. sqrt(6) -> [2, 2, 4]
    http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
    """
    m = 0
    d = 1
    a0 = a = int(sqrt(num))

    expansion = [a0]

    while a != 2*a0:
        m = d*a - m
        d = (num - m*m)//d
        a = (a0 + m)//d
        expansion.append(a)

    return expansion


def convergent_fractions(quotients):
    """
    Get convergent fractions resulting from the quotients
    http://en.wikipedia.org/wiki/Continued_fraction#Continued_fraction_expansions_of_.CF.80
    """
    num, den, prev_num, prev_den = next(quotients), 1, 1, 0

    while True:
        yield num, den
        q = next(quotients)
        prev_num, num, prev_den, den = num, prev_num + num*q, den, prev_den + den*q


def triangle_exists(a, b, c):
    """Check if a triangle with three given side lengths exists"""
    return a + b > c and b + c > a and c + a > b


def arithmetic_series(first, last, terms):
    """Return the sum of the members of a finite arithmetic progression"""
    return terms * (first + last) // 2


def is_square(num):
    """Check if a number is a perfect square. Return isqrt or False."""
    if num % 10 in {2, 3, 7, 8}:
        return False
    root = isqrt(num)
    if num == root*root:
        return root
    return False


def exp_by_squaring(x, n):
    """
    Implements the "exponentiation by squaring" algorithm (iterative version).
    Works for powers >= 1.
    """
    result = 1

    while n > 1:
        if n & 1:
            result *= x
        x *= x
        n //= 2

    return x * result
