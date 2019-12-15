#!/usr/bin/env python

"""Problem 51: Prime digit replacements"""

from utils import is_prime, prime_sieve_lazy


def main():
    for prime in prime_sieve_lazy():
        if prime < 10**4:  # rewind to the first 5-digit prime
            continue

        s = str(prime)

        # we're searching from low to high
        for digit in "012":
            count = s.count(digit)

            # Some observaions:
            #  * count has to be a multiple of 3, otherwise some of the new
            #    primes will be divisible by 3.
            #  * the rightmost digit can't be replaced (it could only be "1")
            if count and not count % 3 and not digit == "1" == s[-1]:
                cnt = 1

                for i in range(int(digit)+1, 10):
                    if i - cnt > 2:
                        break

                    if is_prime(int(s.replace(digit, str(i), count))):
                        cnt += 1
                        if cnt == 8:
                            return prime

if __name__ == '__main__':
    print(main())
