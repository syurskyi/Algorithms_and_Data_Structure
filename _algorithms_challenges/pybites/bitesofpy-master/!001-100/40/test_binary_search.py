from string import ascii_lowercase

from binary_search import binary_search

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)


def test_binary_search_prime():
    assert binary_search(PRIMES, 2) == 0
    assert binary_search(PRIMES, 59) == 16
    assert binary_search(PRIMES, 5) == 2
    assert binary_search(PRIMES, 61) == 17
    assert binary_search(PRIMES, 18) == None


def test_binary_search_alpha():
    assert binary_search(ALPHABET, 'u') == 20
    assert binary_search(ALPHABET, 'a') == 0
    assert binary_search(ALPHABET, 'z') == 25